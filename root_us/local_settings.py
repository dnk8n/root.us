from aredis import StrictRedis

REDIS_CLIENT = StrictRedis(host='127.0.0.1', port=6379, db=0)
