"""
This File contains all routes of Webapp like Controllers in frameworks MVC
Every Model have one Controller in flask controller==BluePrint
http://flask.pocoo.org/docs/1.0/blueprints/

"""

from restfullflask import app
from flask import render_template
# noinspection PyUnresolvedReferences
from restfullflask.models import Pedido
from restfullflask.oficina.routes import oficinaController
from restfullflask.producto.routes import productoController
from restfullflask.repventa.routes import repventaController
from restfullflask.cliente.routes import clienteController

"""
Main BluePrint
"""


@app.route("/")
def home():
    return render_template("index.html")


app.register_blueprint(oficinaController)

app.register_blueprint(productoController)

app.register_blueprint(repventaController)

app.register_blueprint(clienteController)
