import redis
from rediscommon import cache

def storeUserName(username):
    if (cache.get(username) is None):
        cache.append(username,"Nothing yet")
    

def getUserInfo(username):   
    return cache.get(username)