from flask import Blueprint,render_template



# BluePrint MainController
mainController = Blueprint('mainController', __name__, template_folder='templates')

@mainController.route('/')

def index():
    return render_template('index.html')


# BluePrint MainController

articulos=Blueprint('articulos', __name__, template_folder='templates')

@articulos.route('/articulos')

def index():

    return render_template('index2.html')

