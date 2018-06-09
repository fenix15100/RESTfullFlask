import os
from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from application.Controller import mainController,articulos


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

#BluePrints
app.register_blueprint(mainController)
app.register_blueprint(articulos)


#####

db=SQLAlchemy(app)



#Run app
if __name__ == '__main__':
    app.run()


















