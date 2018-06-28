import os
from flask import Flask,render_template,Blueprint
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

#Configuration Flask APP
project_dir=os.path.dirname(os.path.realpath(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+os.path.join(project_dir,"mydb.db")
app.config['DEBUG'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_ECHO']= True

#Bind models of the app in ORM SQLAlchemy
db=SQLAlchemy(app)

#Import my models

from models import *

#Declare my views

oficinaController=Blueprint('oficinaController', __name__, url_prefix='/oficina')

@oficinaController.route('/')
def showAll():

    oficinas=db.session.query(Oficina).all()

    return render_template('oficina_list.html',oficinas=oficinas)


#Register my views
app.register_blueprint(oficinaController)






#main view
@app.route("/")
def home():
    return render_template("index.html")

#Entry Point for the app
if __name__ == "__main__":

    #IF need recreate db uncommnet this
    #db.drop_all()
    #db.create_all()

    app.run()