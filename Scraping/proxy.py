import requests
from bs4 import BeautifulSoup
import csv
from random import choice, uniform
from time import sleep

"""
Proxies:
162.8.230.7:11180
149.202.34.1043:128
162.8.230.7:443
123.84.13.240:8118
109.236.113.30:8080
107.17.92.18:8080
37.191.41.113:8080
112.214.73.253:80
75.151.213.85:8080
61.5.207.102:80
43.254.125.244:80

User-agents:
Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)
Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/5.0)
Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/4.0; InfoPath.2; SV1; .NET CLR 2.0.50727; WOW64)
Mozilla/5.0 (compatible; MSIE 10.0; Macintosh; Intel Mac OS X 10_7_3; Trident/6.0)
Mozilla/1.22 (compatible; MSIE 10.0; Windows 3.1)
Mozilla/5.0 (Windows; U; MSIE 9.0; WIndows NT 9.0; en-US)
Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)
Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 7.1; Trident/5.0)
"""

def get_html(url, useragent=None, proxy=None):
	print('get_html')
	r = requests.get(url, headers=useragent, proxies=proxy)
	return r.text

def get_ip(html):
	soup = BeautifulSoup(html,'lxml')
	ip = soup.find('span', class_='ip').text.strip()
	ua = soup.find('span', class_='ip').find_next_sibling('span').text.strip()

	print(ip)
	print(ua)
	print('--------------------------')

def main():
	url = 'http://sitespy.ru/my-ip'
	
	useragents = open('useragents.txt').read().split('\n')
	proxies = open('proxies.txt').read().split('\n')

	for i in range(10):
		sleep(uniform(1,5))

		print('New Proxy & User-Agent')
		proxy = {'http': 'http://' + choice(proxies)}
		useragent = {'User-Agent': choice(useragents)}
		try:
			html = get_html(url, useragent, proxy)
		except:
			continue
		get_ip(html)

if __name__ == '__main__':
	main()
