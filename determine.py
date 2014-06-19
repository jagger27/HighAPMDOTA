import redis

r = redis.StrictRedis(host='localhost', port=6379, db=0)

def findCounter(r, hero, n=1):
	pipe = r.pipeline()

	pipe.zrevrange('vs '+hero, 0, n-1, 'WITHSCORES')

	return pipe.execute()

	return pipe.execute()

def rateCounter(r, team1, team2):
	score = []

	pipe = r.pipeline()

	c = 0
	for h in team1:
		for g in team2:
			score[c] += r.zscore(g, h)
		c += 1

	return score