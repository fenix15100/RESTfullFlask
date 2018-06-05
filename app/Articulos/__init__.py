from flask import Blueprint, render_template, abort

#BLUEPRINT(Controlador para los colegas)
Articulos = Blueprint('Articulos', __name__,
                        template_folder='templates')
@Articulos.route('/Articulos',methods=["GET"])
def list():
    return render_template("prueba.html")

