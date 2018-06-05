from flask import Flask,render_template
import os
from app.Articulos import Articulos

#Funcion que retorna mi aplicacion FLASK, la creo, registro los submodulos y especifico su configuracion
#Segun la variable de entorno 'FLASK_ENV'
def createapp():

    app = Flask(__name__)
    app.register_blueprint(Articulos)

    if os.environ['FLASK_ENV'] =='development':

        app.config.from_mapping(
            SQLALCHEMY_ECHO=True,
            DEBUG=True,
            SECRET_KEY='dev'


        )
    elif os.environ['FLASK_ENV'] =='production':
        app.config.from_mapping(
            SQLALCHEMY_ECHO=False,
            DEBUG=False,
            SECRET_KEY='prod'

        )

    @app.route('/')
    def index():
        return render_template("home.html")

    return app