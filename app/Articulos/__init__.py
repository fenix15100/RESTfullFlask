from flask import Blueprint, render_template, abort

Articulos = Blueprint('Articulos', __name__,
                        template_folder='templates/Articulos')
@Articulos.route('/Articulos')
def list():
    return "HOLA ARTICULOS"