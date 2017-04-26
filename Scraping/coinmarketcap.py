import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import numpy as np
import pandas as pd
from multiprocessing import Pool


def get_html(url):
	r = requests.get(url)
	return r.text

def get_all_links(html):
	soup = BeautifulSoup(html, 'lxml')

	tds = soup.find('table', id='currencies-all').find_all('td', class_='currency-name')
	links = []

	for td in tds:
		a = td.find('a').get('href')
		link = 'https://coinmarketcap.com' + a
		links.append(link)

	return links

def get_page_data(html):
	soup = BeautifulSoup(html, 'lxml')

	try:
		name = soup.find('h1', class_='text-large').text.strip()
	except:
		name = ''

	try:
		price = soup.find('span', id='quote_price').text.strip()
	except:
		price = ''

	data = {'name': name,
			'price': price}
		
	return data
	# return [name, price]


def write_csv(data):
	with open('coinmarketcap.csv', 'a') as f:
		writer = csv.writer(f)

		writer.writerow( (data['name'],
						  data['price']) )

		# print (data['name'], 'parsed')


def make_all(url):
		html = get_html(url)
		data = get_page_data(html)
		write_csv(data)

def main():
	start = datetime.now()
	url = 'https://coinmarketcap.com/all/views/all/'

	all_links = get_all_links(get_html(url))
	
	arr = np.empty((0,2))

	# for i in all_links:
	# 	html = get_html(i)
	# 	data = get_page_data(html)
	# 	# write_csv(data)
	# 	arr = np.vstack((arr, np.array(data)))

	with Pool(40) as p:
		p.map(make_all, all_links)

	end = datetime.now()
	
	# df = pd.DataFrame(arr, columns=['Name', 'Price'])
	# # print(df)
	# df.to_csv('coin.csv')

	# np.savetxt('arr.txt', arr, delimiter=' ')

	total = end - start
	print (str(total))

if __name__ == '__main__':
	main()
