import os
import secrets
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_modus import Modus
from flask_bootstrap import Bootstrap


app = Flask(__name__)

# Configuration Flask APP
project_dir = os.path.dirname(os.path.realpath(__file__))
#app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(project_dir, "mydb.db")
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://postgres:1234@localhost:5432/training"
app.config['DEBUG'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = str(secrets.token_hex(16))

# Override HTTPMethods
modus = Modus(app)

# Bootstrap vendor
Bootstrap(app)

# init ORM SQLAlchemy
db = SQLAlchemy(app)



# db.engine.execute('PRAGMA foreign_keys = ON;')




# noinspection PyUnresolvedReferences
# My Logic
from restfullflask import routes

