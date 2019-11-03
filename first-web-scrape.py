###STEP 1: importing libraries that make it possible to scrape website###
from bs4 import BeautifulSoup
import requests, mechanize
import csv

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
soup = BeautifulSoup(html, "html.parser")