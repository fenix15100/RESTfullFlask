from flask import render_template, Blueprint, request, redirect, flash, url_for
from restfullflask.cliente.models import db, Cliente
from restfullflask.cliente.forms import ClienteForm

"""
Cliente BluePrint
"""

clienteController = Blueprint('clienteController', __name__, template_folder='templates/')
