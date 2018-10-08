from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from bs4 import BeautifulSoup
import re,time,yagmail,logging,os
from config import *
try:
    LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
    logging.basicConfig(filename="./logs.log",level=logging.INFO,format=LOG_FORMAT,filemode="a")
    logger= logging.getLogger()

    yag=yagmail.SMTP(EMAIL_USERNAME, EMAIL_PASSWORD,host="smtp.office365.com",port="587",smtp_starttls=True,smtp_ssl=False)

    firefox_options = Options()
    #firefox_options.add_argument("--headless")
    driver = webdriver.Firefox(firefox_options=firefox_options, executable_path=FIREFOX_DRIVER)

    def send_email(status,message):
        yag.send(to=TO_EMAIL,subject="Rebuild Code: {}".format(status),contents=message)
        logging.info("Mail Sent!")
    driver.get(r"https://ma.maxnow.com/app/serveradmin?action=Indexes.view")
    username=driver.find_element_by_name("username")
    username.send_keys(USERNAME)

    password=driver.find_element_by_name("password")
    password.send_keys(PASSWORD)

    submit=driver.find_element_by_name("submit")
    submit.click()

    time.sleep(3)
    driver.get("https://ma.maxnow.com/app/serveradmin?action=Index.rebuild&index=ASSET")
    time.sleep(5)

    while True:
        try:
            soup=BeautifulSoup(driver.page_source,"lxml")
            complete_text=str(soup.find_all("tbody")[2]).strip() #.find_all("tr")[2].find_all("td")[2].text.strip()
            status=re.search(r"Rebuild code:(.*)?<br/>",complete_text)
            if status is not None:
                status=status.group(1).strip()
            else:
                status="ERROR"
            if status=="Complete":
                message=re.search(r"Rebuild message:(.*)?</td>",complete_text).group(1).strip()
                logging.info("Complete!")
                send_email(status,message)
                driver.quit()
                break
            elif status=="Running":
                index_link=driver.find_element_by_link_text("Index Rebuild Status")
                index_link.click()
                time.sleep(5)
                print("Running....")
                logging.info("Running....")
                continue
            # elif status=="Error":
            #     rebuild_link=driver.find_element_by_link_text("Rebuild")
            #     rebuild_link.click()
            #     time.sleep(5)
            #     print("Error....")
            #     continue
            else:
                time.sleep(5)
                driver.get("https://ma.maxnow.com/app/serveradmin?action=Index.rebuild&index=ASSET")
                print("Something Gone Wrong....")
                logging.info("Something Gone Wrong....")
                time.sleep(5)
                continue
        except Exception as e:
            print("ERROR:",e)
            logger.error("ERROR:{}".format(str(e)))
            continue
except Exception as e:
    logger.error("ERROR outside "+str(e))