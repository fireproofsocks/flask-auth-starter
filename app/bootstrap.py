# ---------------------------------
# Create The Server Application
# ---------------------------------
from flask import Flask
server = Flask(__name__, static_folder='./public', static_url_path='')
