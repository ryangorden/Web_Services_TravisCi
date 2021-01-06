from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# Create Flask application, load configuration ,and
# create the SQLAlchemy object
basedir= os.path.abspath(os.path.dirname(__file__))
app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///' + os.path.join(basedir, 'network.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

