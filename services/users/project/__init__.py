# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 21:03:23 2019

@author: tommy
"""

from flask import Flask, jsonify


#instantiate the app
app = Flask(__name__)

# set config
app.config.from_object('project.config.DevelopmentConfig')

@app.route('/users/ping', methods=['GET'])
def ping_pong():
    return jsonify({
            'status': 'success',
            'message': 'pong'
    })