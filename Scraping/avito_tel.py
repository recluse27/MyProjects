from selenium import webdriver
from time import sleep
from PIL import Image
from pytesseract import image_to_string


class Bot:
	def __init__(self):
		# self.driver = webdriver.Firefox()
		self.driver = webdriver.PhantomJS()
		self.navigate()

	def take_screenshot(self):
		self.driver.save_screenshot('avito_screenshot.png')

	def tel_recon(self):
		image = Image.open('tel.gif')
		print (image_to_string(image))



	def crop(self, location, size):
		image = Image.open('avito_screenshot.png')
		x = location['x']
		y = location['y']
		width = size['width']
		height = size['height']

		image.crop((x, y, x+width, y+height)).save('tel.gif')

		self.tel_recon()


	def navigate(self):
		self.driver.get('https://www.avito.ru/moskva/telefony/htc_desire_700_dual_sim_1082546234')
		button = self.driver.find_element_by_xpath('//button[@class="button item-phone-button js-item-phone-button button-origin button-origin-blue button-origin_full-width button-origin_large-extra item-phone-button_hide-phone item-phone-button_card js-item-phone-button_card"]')
		button.click()

		sleep(3)

		self.take_screenshot()

		image = self.driver.find_element_by_xpath('//div[@class="item-phone-big-number js-item-phone-big-number"]//*')
		location = image.location # dict{'x': 2343, 'y': 23423}
		size = image.size		  # dict{'width': 234, 'height': 234}

		self.crop(location, size)




def main():
	# pass
	b = Bot()



if __name__ == "__main__":
	main()
