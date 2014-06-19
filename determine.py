import redis

r = redis.StrictRedis(host='localhost', port=6379, db=0)

def findCounter(r, hero, n=1):
	pipe = r.pipeline()

	pipe.zrevrange('vs '+hero, 0, n-1, 'WITHSCORES')

	return pipe.execute()