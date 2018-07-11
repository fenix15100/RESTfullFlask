from restfullflask.HelpersScripts.wtfhtml5 import IntegerField,DecimalField
from wtforms import Form,StringField,validators


class OficinaForm(Form):
    ciudad = StringField('Ciudad', validators=[validators.Length(max=15,message="Como maximo 15 Caracteres"),validators.DataRequired("Introduce una Ciudad")])
    region = StringField('Region', validators=[validators.Length(max=10,message="Como maximo 10 Caracteres"),validators.DataRequired("Introduce una Región")])
    director = IntegerField('Director')
    objetivo= DecimalField('Objetivo',validators=[validators.DataRequired("Numero decimal Requerido")],places=2)
    ventas = DecimalField('Ventas',validators=[validators.DataRequired("Numero Decimal requerido")],places=2)

    #Set fields from a Model Oficina

    def populateForm(self,Oficina):

        self.ciudad.data=Oficina.ciudad
        self.region.data=Oficina.region
        self.director.data=Oficina.director
        self.objetivo.data=Oficina.objetivo
        self.ventas.data=Oficina.ventas