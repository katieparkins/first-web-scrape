###STEP 1: importing libraries that make it possible to scrape website###
import csv
import requests, mechanize
from bs4 import BeautifulSoup

#create file
csvfile = open('highway.csv', 'a')

#create writer that knows how to interact with the file
highway_writer = csv.writer(csvfile)

###STEP 2: setting up whole url as string so you don't have to type full url everytime###
url = 'https://www.mshp.dps.missouri.gov/HP68/SearchAction?searchDate=10/31/2017'

###Get the HTML!
br = mechanize.Browser()
br.open(url)
html = br.response().read

###STEP 3: Make soup! 
###WHERE ISSUE BEGINS: "TypeError: object of type 'method' has no len()
soup = BeautifulSoup(html, "html.parser")

###STEP 4: Dig through the HTML!
table = soup.find('table', {'id': 'accidentOutput'})
rows = table.find_all('tr')

for row in rows:
	cells = rows.find_all('td')
	data = []
	for cell in cells:
		data.append(cell.text)
	highway_writer.writerow(data)