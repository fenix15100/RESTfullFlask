import os
from flask import Flask,render_template,Blueprint,request,flash,redirect,url_for,_request_ctx_stack
from flask_sqlalchemy import SQLAlchemy
from flask_modus import Modus
from forms import *


app=Flask(__name__)

#Configuration Flask APP
project_dir=os.path.dirname(os.path.realpath(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+os.path.join(project_dir,"mydb.db")
app.config['DEBUG'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_ECHO']= True
app.config['SECRET_KEY']= 'developmentkey'

#Override HTTPMethods
modus = Modus(app)

#Bind models of the app in ORM SQLAlchemy
db=SQLAlchemy(app)


from models import *

#-----------------------------------------------------------------------------------------------------------------------

#Register Views



# main view
@app.route("/")
def home():
    return render_template("index.html")


#BluePrint Oficina

oficinaController = Blueprint('oficinaController', __name__)


@oficinaController.route('/oficinas/',methods=['GET'])
def showAll():
    oficinas = db.session.query(Oficina).all()

    return render_template('oficina_list.html', oficinas=oficinas)


@oficinaController.route('/oficina/',methods=['GET','POST'])
def add():

    form = OficinaForm(request.form)

    if request.method=='POST':
        oficina = Oficina(form.ciudad.data, form.region.data,
                    form.director.data,form.objetivo.data,form.ventas.data)
        db.session.add(oficina)
        db.session.commit()
        flash('Oficina Added!')
        return redirect(url_for('oficinaController.showAll'))


    return render_template('oficina_add.html', form=form)

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


@oficinaController.route('/oficina/<int:id>/',methods=['DELETE'])
def delete(id):

    if request.method == b"DELETE":

        oficina = db.session.query(Oficina).get(id)
        db.session.delete(oficina)
        db.session.commit()
        flash('Oficina Deleted!')
        return redirect(url_for('oficinaController.showAll'))


# Register blueprint oficina
app.register_blueprint(oficinaController)

#---------------------

#-----------------------------------------------------------------------------------------------------------------------


#Entry Point for the app
if __name__ == "__main__":

    #IF need recreate db uncommnet this
    #db.drop_all()
    #db.create_all()

    app.run()