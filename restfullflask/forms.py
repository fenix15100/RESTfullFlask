from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,DecimalField,validators


class OficinaForm(FlaskForm):
    ciudad = StringField('Ciudad', [validators.Length(max=15),validators.input_required])
    region = StringField('Region', [validators.Length(max=10),validators.input_required])
    director = IntegerField('Director')
    objetivo= DecimalField('Objetivo') #,[validators.number_range(max=9),validators.input_required],places=2
    ventas = DecimalField('Ventas') #, [validators.number_range(max=9),validators.input_required], places=2