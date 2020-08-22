"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from flask import Flask, jsonify
from WS import app

#@app.route('/')
@app.route('/test/testGET', methods=['GET'])
def testGet():
    return jsonify({'tasks': 'ola'})
