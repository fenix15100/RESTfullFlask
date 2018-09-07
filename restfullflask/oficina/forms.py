from restfullflask.oficina.models import Oficina
from restfullflask.HelpersScripts.wtfhtml5 import IntegerField, DecimalField
from wtforms import Form, StringField, validators


class OficinaForm(Form):
    ciudad = StringField(label='Ciudad', validators=[validators.Length(max=15, message="Como maximo 15 Caracteres"),
                                               validators.InputRequired("Introduce una Ciudad")])

    region = StringField(label='Region', validators=[validators.Length(max=10, message="Como maximo 10 Caracteres"),
                                               validators.InputRequired("Introduce una Región")])
    director = IntegerField(label='Director')

    objetivo = DecimalField(label='Objetivo', validators=[validators.InputRequired("Campo requerido"),
                                                    validators.NumberRange(min=0, message="El valor tiene que ser mayor o igual a 0")],
                            places=2)

    ventas = DecimalField(label='Ventas', validators=[validators.InputRequired("Numero Decimal requerido"),
                                                validators.NumberRange(min=0, message="El valor tiene que ser mayor o igual a 0")],
                          places=2)

    # Set fields from a Model Oficina

    def populateform(self, oficina: Oficina):
        self.ciudad.data = oficina.ciudad
        self.region.data = oficina.region
        self.director.data = oficina.director
        self.objetivo.data = oficina.objetivo
        self.ventas.data = oficina.ventas
