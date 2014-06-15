from bs4 import BeautifulSoup
import urllib2
import json

p = BeautifulSoup(urllib2.urlopen("http://dotabuff.com/heroes").read())

names = []

for link in p.find_all("div", class_="name"):
	names.append(str(link.string).lower().replace(' ','-').replace("'",''))

print names
