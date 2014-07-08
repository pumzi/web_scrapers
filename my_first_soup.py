from bs4 import BeautifulSoup

import requests


#beautiful soup documentation
# anchor text is the thing you click on that leads to another page

#url = raw_input("Enter a website to extract the URL's from: ")

r  = requests.get("http://noisey.vice.com/en_ca/blog/the-number-one-reason-there-arent-more-female-djs" )

data = r.text

soup = BeautifulSoup(data)


for link in soup.find_all('a'):
    print(link.get('href'))