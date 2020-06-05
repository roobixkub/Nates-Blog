# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 21:56:51 2020

@author: Nate
"""


from flask import Flask

import config
import models

from resources.posts import posts_api


app = Flask(__name__)
app.register_blueprint(posts_api)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    models.initialize()
    app.run(debug=config.DEBUG, host=config.HOST, port=config.PORT)
