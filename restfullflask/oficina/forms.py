from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,DecimalField,validators


class OficinaForm(FlaskForm):
    ciudad = StringField('Ciudad', [validators.Length(max=15),validators.input_required])
    region = StringField('Region', [validators.Length(max=10),validators.input_required])
    director = IntegerField('Director')
    objetivo= DecimalField('Objetivo') #,[validators.number_range(max=9),validators.input_required],places=2
    ventas = DecimalField('Ventas') #, [validators.number_range(max=9),validators.input_required], places=2

    #Set fields from a Model Oficina

    def populateForm(self,Oficina):

        self.ciudad.data=Oficina.ciudad
        self.region.data=Oficina.region
        self.director.data=Oficina.director
        self.objetivo.data=Oficina.objetivo
        self.ventas.data=Oficina.ventas