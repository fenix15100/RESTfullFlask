
from flask import render_template,Blueprint


articulos_blue=Blueprint('articulos',__name__,template_folder='templates')

@articulos_blue.route('/articulos',methods=['GET'])
def index():
    return  render_template("articulos/index.html")