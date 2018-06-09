import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from app.Controller import *





#Load ENV system from file
APP_ROOT = os.path.join(os.path.dirname(__file__), '..')
dotenv_path = os.path.join(APP_ROOT, '.env')
load_dotenv(dotenv_path)


#Instance Flask App from ENV file
app = Flask(__name__)

app.config.from_mapping(
            SQLALCHEMY_ECHO=os.getenv('SQLALCHEMY_ECHO'),
            DEBUG=os.getenv('DEBUG'),
            SECRET_KEY=os.getenv('SECRET_KEY'),
            SQLALCHEMY_DATABASE_URI=os.getenv('SQLALCHEMY_DATABASE_URI'),
            SQLALCHEMY_TRACK_MODIFICATIONS=os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')

        )

app.register_blueprint(main)

#Run app
if __name__ == "__main__":

    app.run()















