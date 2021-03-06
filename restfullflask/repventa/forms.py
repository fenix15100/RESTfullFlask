import datetime

from restfullflask.HelpersScripts.wtfhtml5 import IntegerField, DateRange, DateField, DecimalField
from wtforms import Form, StringField, SelectField, validators
from restfullflask.repventa.models import Repventa, db
from restfullflask.oficina.models import Oficina


class RepventaForm(Form):
    id_empleado = IntegerField(label="ID",
                               validators=[validators.InputRequired("Se debe especificar un ID para el empleado")])

    nombre = StringField(label="Nombre", validators=[validators.Length(max=15, message="Maximo 15 Caracteres"),
                                                     validators.InputRequired("Se debe especificar un nombre")])

    edad = IntegerField(label="Edad", validators=[validators.NumberRange(min=19, message="Debe ser mayor de 18 años")])

    id_oficina = SelectField(label="Oficina", coerce=int)

    id_director = SelectField(label="Director", coerce=int)

    titulo = StringField(label="Titulo", validators=[validators.Length(max=10, message="Maximo 10 Caracteres")])

    contrato = DateField(label="Fecha Contrato",
                         validators=[validators.InputRequired("Es necesaria una fecha de contrato"),
                                     DateRange(
                                         min=datetime.datetime.strptime('1800-01-01', "%Y-%m-%d").date(),
                                         max=datetime.datetime.now().date(), )],
                         default=datetime.datetime.now().date())

    ventas = DecimalField(label="Ventas", places=2, validators=[validators.InputRequired("Campo obligatorio")])

    cuota = DecimalField(label="Cuota", places=2)

    def __init__(self, *args, **kwargs):
        super(RepventaForm, self).__init__(*args, **kwargs)
        self.id_oficina.choices = [(-1, "---")] + [(oficina.id_oficina, oficina.ciudad) for oficina in
                                                   db.session.query(Oficina).all()]
        self.id_director.choices = [(-1, "---")] + [(repventa.id_empleado, repventa.nombre) for repventa in
                                                    db.session.query(Repventa).all()]


    def populateform(self, repventa: Repventa):
        self.id_empleado.data=repventa.id_empleado
        self.nombre.data=repventa.nombre
        self.id_oficina.data=repventa.id_oficina
        self.id_director.data=repventa.id_director
        self.edad.data=repventa.edad
        self.contrato.data=repventa.contrato
        self.ventas.data=repventa.ventas
        self.cuota.data=repventa.cuota
        self.titulo.data=repventa.titulo
