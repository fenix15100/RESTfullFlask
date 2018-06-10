import os
from flask import Flask,render_template
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy



#Load ENV system from file
project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "mydb.db"))
APP_ROOT = os.path.join(os.path.dirname(__file__), '..')
dotenv_path = os.path.join(APP_ROOT, '.env')
load_dotenv(dotenv_path)



#Instance Flask App from ENV file
app = Flask(__name__)


app.config.from_mapping(
            SQLALCHEMY_ECHO=os.getenv('SQLALCHEMY_ECHO'),
            DEBUG=os.getenv('DEBUG'),
            SECRET_KEY=os.getenv('SECRET_KEY'),
            SQLALCHEMY_DATABASE_URI=database_file,
            SQLALCHEMY_TRACK_MODIFICATIONS=os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')

        )



db=SQLAlchemy(app)
class Articulos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)


    def __repr__(self):
        return '<Name %r>' % self.name




@app.route('/',methods=['GET'])
def root():

    return render_template('index.html')

from .articulos.views import articulos_blue

app.register_blueprint(articulos_blue)

