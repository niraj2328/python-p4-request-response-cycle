#!/usr/bin/env python3

import os

from flask import Flask, request, g

app = Flask(__name__)

@app.before_request
def set_path():
    g.path = os.path.abspath(os.getcwd())

@app.route('/')
def index():
    host = request.headers.get('Host')
    appname = app.name
    response_body = f'''
        <h1>The host for this page is {host}</h1>
        <h2>The name of this application is {appname}</h2>
        <h3>The path of this application on the user's device is {g.path}</h3>
    '''

    status_code = 200
    headers = {}

    return response_body, status_code, headers

if __name__ == '__main__':
    app.run(port=5555, debug=True)
