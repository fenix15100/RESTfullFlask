from restfullflask.oficina.models import Oficina
from restfullflask.HelpersScripts.wtfhtml5 import IntegerField, DecimalField
from wtforms import Form, StringField, validators


class OficinaForm(Form):
    ciudad = StringField('Ciudad', validators=[validators.Length(max=15, message="Como maximo 15 Caracteres"),
                                               validators.InputRequired("Introduce una Ciudad")])
    region = StringField('Region', validators=[validators.Length(max=10, message="Como maximo 10 Caracteres"),
                                               validators.InputRequired("Introduce una Región")])
    director = IntegerField('Director')
    objetivo = DecimalField('Objetivo', validators=[validators.InputRequired("Numero decimal Requerido")], places=2)
    ventas = DecimalField('Ventas', validators=[validators.InputRequired("Numero Decimal requerido")], places=2)

    # Set fields from a Model Oficina

    def populateform(self, oficina: Oficina):
        self.ciudad.data = oficina.ciudad
        self.region.data = oficina.region
        self.director.data = oficina.director
        self.objetivo.data = oficina.objetivo
        self.ventas.data = oficina.ventas
