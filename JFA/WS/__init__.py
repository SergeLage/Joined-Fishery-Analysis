"""
The flask application package.
"""

from flask import Flask
app = Flask(__name__)

import WS.test_api
import WS.api
