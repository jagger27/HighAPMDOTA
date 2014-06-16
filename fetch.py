from bs4 import BeautifulSoup as Soup
import urllib2
import redis

class RedisConnection(object):
	def __init__(self):
		self.r = redis.StrictRedis(host='localhost', port=6379, db=0)

def parseMatchup(hero, r):
	heroHTML = Soup(fetchHero(hero))
	pipe = r.pipeline()

	for link in heroHTML.find_all("a", class_="hero-link"):
		pipe.zadd(str(hero),
				  float(link.parent.find_next_sibling().contents[0][:-1]),
				  str(link.string))
		# advantages[str(link.string)] = float(link.parent.find_next_sibling().contents[0][:-1])
	pipe.execute()

def fetchHero(hero):
	return urllib2.urlopen("http://dotabuff.com/heroes/" + str(hero) + "/matchups").read()

def fetchHeroList():
	return urllib2.urlopen("http://dotabuff.com/heroes").read()