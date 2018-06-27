import os
from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

#En algun momento ira por ENV file
project_dir=os.path.dirname(os.path.realpath(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+os.path.join(project_dir,"mydb.db")
app.config['DEBUG'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_ECHO']= True

db=SQLAlchemy(app)


from models import *




@app.route("/")
def hello():
    return render_template("index.html")


if __name__ == "__main__":
    db.drop_all()
    db.create_all()
    app.run()