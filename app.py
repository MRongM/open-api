from flask import Flask
import os
import logging
import redis
import gevent

app = Flask(__name__)
app.debug = 'DEBUG' in os.environ


@app.route('/')
def hello_world():
    return 'hello world'
