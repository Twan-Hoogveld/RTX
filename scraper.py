from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import platform
import pickle
import sys
import requests
import time

class Card:
	def __init__(self, url, name ):
		self.URL = url
		self.name= name

if __name__ == '__main__':
	#Options for a headless chrome webdriver.
	options = webdriver.ChromeOptions()
	#options.add_argument('headless')
	options.add_argument("disable-gpu")

	#Check platform.
	if platform.system() == 'Windows':
		#Webdriver for Windows
		driver = webdriver.Chrome("C:\\chromedriver\\chromedriver.exe",options=options)
	else:
		#Webdriver for Linux
		driver = webdriver.Chrome("/usr/local/bin/chromedriver",options=options)

	#Get the webpage with all the GTX 3000 cards on it
	driver.get("https://tweakers.net/videokaarten/vergelijken/#filter:q1YqSExPDc6sSlWyMjQw0FEqKMpMTvXNzFOyAnKKC1KT3TJzSlKLipWsqpWMjEBkWWKOklW0kqGFoamZkg6YtlCKra2tBQA")

	#Accepts The Coockies
	accept_button = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='cookieAcceptForm']/span/button")))
	accept_button.click()

	#Make it readable
	content = driver.page_source
	soup = BeautifulSoup(content,features="html.parser")

	#Turn all the results into Class object so we can iterate over it later.
	cards = []
	for a in soup.findAll('a',href=True, attrs={'class':'editionName'}):
		cards.append(Card(name=a.text,url=a['href']))

	#Click the link for every card
	for card in cards:
		time.sleep(10)
		driver.get(card.URL)
		time.sleep(10)
		content = driver.page_source
		soup = BeautifulSoup(content,features="html.parser")

		#Loop through all the shops and check if you can order.
		shops = []
		for a in soup.findAll('a',href=True, attrs={'class':'shop-listing'}):
			print(a)
			print(a.text)
