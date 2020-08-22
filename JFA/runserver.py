"""
This script runs the JFA application using a development server.
"""

from os import environ
from AS.classifier import Classifier
from WS import app

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    Classifier.start()
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, 5555)
    #port='80'