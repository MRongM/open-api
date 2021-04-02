from flask import Flask
import os
import logging
import gevent

app = Flask(__name__)
app.debug = 'DEBUG' in os.environ


@app.route('/')
def hello_world():
    return 'hello world'

@app.route('/test')
def foo():
    return "ok"

@app.route('/abi')
def bar():
    return {"A":"C",1:123}
