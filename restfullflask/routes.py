"""
This File contains all routes of Webapp like Controllers in frameworks MVC
Every Model have one Controller in flask controller==BluePrint
http://flask.pocoo.org/docs/1.0/blueprints/

"""

from restfullflask import app,db
from flask import render_template,Blueprint,request,redirect,flash,url_for
from restfullflask.models import *
from restfullflask.forms import *

###Main  Blueprint----------------------------------------------------------
@app.route("/")
def home():
    return render_template("index.html")



###BluePrint Oficina---------------------------------------------------------

oficinaController = Blueprint('oficinaController', __name__)


#Action (Get all entrys for a model "Oficina" and send array to template)
@oficinaController.route('/oficinas/',methods=['GET'])
def showAll():
    oficinas = db.session.query(Oficina).all()

    return render_template('oficina_list.html', oficinas=oficinas)


#Action (Add entry for a model "Oficina" and redirect to Action "ShowAll")
@oficinaController.route('/oficina/',methods=['GET','POST'])
def add():

    #Render a valid HTML5 form for handle data to Add a new entry "Oficina"
    form = OficinaForm(request.form)

    if request.method=='POST':

        oficina = Oficina(form.ciudad.data, form.region.data,
                    form.director.data,form.objetivo.data,form.ventas.data)
        db.session.add(oficina)
        db.session.commit()
        flash('Oficina Added!')
        return redirect(url_for('oficinaController.showAll'))


    return render_template('oficina_add.html', form=form)

#Action (Edit one Entry for model "Oficina" and redirect to Action "ShowAll")
@oficinaController.route('/oficina/<int:id>/',methods=['GET','PUT'])
def edit(id):

    oficina=db.session.query(Oficina).get(id)
    form = OficinaForm(request.form)

    if request.method==b"PUT":
        oficina.ciudad=form.ciudad.data
        oficina.region=form.region.data
        oficina.director=form.director.data
        oficina.objetivo=form.objetivo.data
        oficina.ventas=form.ventas.data
        db.session.commit()
        flash('Oficina Updated!')
        return redirect(url_for('oficinaController.showAll'))


    form.ciudad.data = oficina.ciudad
    form.region.data = oficina.region
    form.director.data = oficina.director
    form.objetivo.data = oficina.objetivo
    form.ventas.data = oficina.ventas

    return render_template('oficina_edit.html', form=form,id=id)

#Action (Delete one Entry for model "Oficina" and redirect to Action "ShowAll")
@oficinaController.route('/oficina/<int:id>/',methods=['DELETE'])
def delete(id):

    if request.method == b"DELETE":

        oficina = db.session.query(Oficina).get(id)
        db.session.delete(oficina)
        db.session.commit()
        flash('Oficina Deleted!')
        return redirect(url_for('oficinaController.showAll'))

#Register blueprint oficina
app.register_blueprint(oficinaController)