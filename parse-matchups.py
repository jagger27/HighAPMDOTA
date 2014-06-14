from bs4 import BeautifulSoup
import urllib2
import json

p = BeautifulSoup(urllib2.urlopen("http://dotabuff.com/heroes/huskar/matchups").read())

hero = p.h1.contents[0]

advantages = dict()

for link in p.find_all("a", class_="hero-link"):
	# print (str(link.string), float(link.parent.find_next_sibling().contents[0][:-1]))
	advantages[str(link.string)] = float(link.parent.find_next_sibling().contents[0][:-1])

print advantages
print json.dumps([hero, advantages], sort_keys=True, indent=2, separators=(',', ': '))