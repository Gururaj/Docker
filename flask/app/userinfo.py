import redis
from rediscommon import cache

def storeUserName(username):
    cache.append(username,"Nothing yet")

def getUserInfo(username):
    return cache.get(username)