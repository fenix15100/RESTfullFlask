import datetime

from restfullflask.HelpersScripts.wtfhtml5 import IntegerField,DateRange,DateField
from wtforms import Form, StringField, SelectField, validators
from restfullflask.repventa.models import Repventa
from restfullflask.oficina.models import Oficina, db

# TODO Finish Form
class RepventaForm(Form):
    id_empleado = IntegerField(label="ID",
                               validators=[validators.DataRequired("Se debe especificar un ID para el empleado")])

    nombre = StringField(label="Nombre", validators=[validators.Length(max=15, message="Maximo 15 Caracteres"),
                                                     validators.DataRequired("Se debe especificar un nombre")])

    edad = IntegerField(label="Edad", validators=[validators.NumberRange(min=19, message="Debe ser mayor de 18 años")])

    # TODO fix dinamic selectquery
    id_oficina = SelectField(label="Oficina", choices=[(oficina.id_oficina, oficina.ciudad) for oficina in
                                                       db.session.query(Oficina).all()], coerce=int)

    titulo = StringField(label="Titulo", validators=[validators.Length(max=10,message="Maximo 10 Caracteres")])

    contrato = DateField(label="Fecha", validators=[validators.DataRequired("Es necesaria una fecha de contrato"),
                                                    DateRange(min=datetime.datetime.strptime('1800-01-01', "%Y-%m-%d").date(),
                                                              max=datetime.datetime.now().date(),)],
                         default=datetime.datetime.now().date())



    # TODO Implement method
    def populateform(self, repventa: Repventa):
        pass

