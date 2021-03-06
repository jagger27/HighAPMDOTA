from bs4 import BeautifulSoup as Soup
import urllib2
import redis

def parseMatchup(hero, pipe):
	heroHTML = Soup(fetchHero(hero))

	for link in heroHTML.find_all("a", class_="hero-link"):
		pipe.zadd(str(hero),
				  float(link.parent.find_next_sibling().contents[0][:-1]),
				  str(link.string))
		# advantages[str(link.string)] = float(link.parent.find_next_sibling().contents[0][:-1])

def fetchHero(hero):
	return urllib2.urlopen("http://dotabuff.com/heroes/" + str(hero).lower().replace(' ','-').replace("'",'') + "/matchups").read()

def fetchHeroList():
	return urllib2.urlopen("http://dotabuff.com/heroes").read()

def parse(r):
	pipe = r.pipeline()

	listHTML = Soup(fetchHeroList())

	for link in listHTML.find_all("div", class_="name"):
		hero = str(link.string)
		parseMatchup(hero, pipe)

	pipe.execute()

r = redis.StrictRedis(host='localhost', port=6379, db=0)

def makeReverseLookupTables(r):
	pipe = r.pipeline()

	listHTML = Soup(fetchHeroList())
	heroes = []
	for link in listHTML.find_all("div", class_="name"):
		heroes.append(str(link.string))

	print len(heroes)

	for h in heroes:
		for other in rem(heroes, h):
			pipe.zadd('vs ' + h, pipe.zscore(other, h), other)

	pipe.execute()

def rem(li, i):
	new = list(li)
	new.remove(i)
	return new

# parse(r)
