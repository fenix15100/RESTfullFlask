from flask import Blueprint,render_template

# BluePrint MainController
main = Blueprint('main', __name__, template_folder='templates')

@main.route('/')

def index():
    return render_template('index.html')


# BluePrint MainController
