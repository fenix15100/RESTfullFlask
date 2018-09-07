import datetime

from restfullflask.HelpersScripts.wtfhtml5 import IntegerField, DateRange, DateField, DecimalField
from wtforms import Form, StringField, SelectField, validators
from restfullflask.repventa.models import Repventa, db
from restfullflask.oficina.models import Oficina


# TODO fix issue wtf form convert 0 integer value to False Boolean  and cause error in server validation
class RepventaForm(Form):
    id_empleado = IntegerField(label="ID",
                               validators=[validators.DataRequired("Se debe especificar un ID para el empleado")])

    nombre = StringField(label="Nombre", validators=[validators.Length(max=15, message="Maximo 15 Caracteres"),
                                                     validators.DataRequired("Se debe especificar un nombre")])

    edad = IntegerField(label="Edad", validators=[validators.NumberRange(min=19, message="Debe ser mayor de 18 años")])

    id_oficina = SelectField(label="Oficina", coerce=int)

    id_director = SelectField(label="Director", coerce=int)

    titulo = StringField(label="Titulo", validators=[validators.Length(max=10, message="Maximo 10 Caracteres")])

    contrato = DateField(label="Fecha Contrato",
                         validators=[validators.DataRequired("Es necesaria una fecha de contrato"),
                                     DateRange(
                                         min=datetime.datetime.strptime('1800-01-01', "%Y-%m-%d").date(),
                                         max=datetime.datetime.now().date(), )],
                         default=datetime.datetime.now().date())

    ventas = DecimalField(label="Ventas", places=2, validators=[validators.DataRequired("Campo obligatorio")])

    cuota = DecimalField(label="Cuota", places=2)

    def __init__(self, *args, **kwargs):
        super(RepventaForm, self).__init__(*args, **kwargs)
        self.id_oficina.choices = [(-1, "---")] + [(oficina.id_oficina, oficina.ciudad) for oficina in
                                                   db.session.query(Oficina).all()]
        self.id_director.choices = [(-1, "---")] + [(repventa.id_empleado, repventa.nombre) for repventa in
                                                    db.session.query(Repventa).all()]

    # TODO Implement method
    def populateform(self, repventa: Repventa):
        pass
