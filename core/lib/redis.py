import redis
import sys

pool = redis.ConnectionPool(host=sys.argv[2], port=sys.argv[3])

r = redis.Redis(connection_pool=pool)
