from bs4 import BeautifulSoup

import requests

#I want to scrape all of the venues that are on this webpage

url = "http://www.dclivemusic.com/venues.php"
r  = requests.get(url)

data = r.text

soup = BeautifulSoup(data)

#print(soup.get_text())

body = soup.findAll('p')

if "20010" in body:
	print "Uptown 4 eva"
else:
	print "Move on!"
#We want to print out the title of the site 

title = soup.title.text

#if/else statement to make sure I am on the right webpage

if "Live music venues" in title:
	print "you are in the live venue page"
else: 
	print "Get off this page"

# I want to scrape all of the links.
#for link in soup.find_all('a'):
 #   print(link.get('href'))