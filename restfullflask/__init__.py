import os
import secrets
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_modus import Modus


app=Flask(__name__)

#Configuration Flask APP
project_dir=os.path.dirname(os.path.realpath(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+os.path.join(project_dir,"mydb.db")
app.config['DEBUG'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_ECHO']= True
app.config['SECRET_KEY']= str(secrets.token_hex(16))

#Override HTTPMethods
modus = Modus(app)

#init ORM SQLAlchemy
db=SQLAlchemy(app)

#My Logic
from restfullflask import routes


