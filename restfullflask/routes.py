"""
This File contains all routes of Webapp like Controllers in frameworks MVC
Every Model have one Controller in flask controller==BluePrint
http://flask.pocoo.org/docs/1.0/blueprints/

"""

from restfullflask import app
from flask import render_template


"""
Main BluePrint
"""
@app.route("/")
def home():
    return render_template("index.html")

#Importo los modelos de forma temporal, la idea es que los llamen sus Blueprints cuando este hecho

from restfullflask.models import *

from restfullflask.oficina.routes import oficinaController
app.register_blueprint(oficinaController)