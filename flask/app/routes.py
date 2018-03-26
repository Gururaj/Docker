from flask import render_template, flash, redirect, session, url_for, request, g, Markup
from app import app
from hits import get_hit_count
from userinfo import storeUserName, getUserInfo

@app.route('/')
def getCount():
    count = get_hit_count()
    return 'Hello World! I have been seen {} times.\n'.format(count)
    
@app.route('/<username>')
def storeAndGetUserName(username):
    storeUserName(username)
    return "Stored %s with %s information" % (username, getUserInfo(username))