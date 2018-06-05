import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


# SHELL set FLASK_APP=app:createapp set FLASK_ENV=development or production
def createapp():

    app = Flask(__name__)

    app = registerModels(config(app))

    @app.route('/',methods=["GET"])
    def index():
        return render_template("home.html")

    return app


def config(app):

    if os.environ['FLASK_ENV'] == 'development':

        app.config.from_mapping(
            SQLALCHEMY_ECHO=True,
            DEBUG=True,
            SECRET_KEY='dev',
            SQLALCHEMY_DATABASE_URI=database_file,
            SQLALCHEMY_TRACK_MODIFICATIONS=True

        )
    elif os.environ['FLASK_ENV'] == 'production':
        app.config.from_mapping(
            SQLALCHEMY_ECHO=False,
            DEBUG=False,
            SECRET_KEY='prod',
            SQLALCHEMY_DATABASE_URI=database_file,
            SQLALCHEMY_TRACK_MODIFICATIONS=True

        )
    return app

def registerModels(app):
    from app.Articulos import Articulos

    app.register_blueprint(Articulos)

    return app

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "mydb.db"))
db = SQLAlchemy(createapp())

