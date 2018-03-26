import time 
import redis 

from flask import render_template, flash, redirect, session, url_for, request, g, Markup
from app import app

cache = redis.Redis(host='redis', port=6379)

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)


@app.route('/')
def hello_world():
    count = get_hit_count()
    return 'Hello World! I have been seen {} times.\n'.format(count)
    # return 'Hello World!.\n'