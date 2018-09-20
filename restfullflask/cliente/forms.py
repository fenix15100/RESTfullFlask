from restfullflask.cliente.models import Cliente
from restfullflask.HelpersScripts.wtfhtml5 import IntegerField, DecimalField
from wtforms import Form, StringField, validators

class ClienteForm(Form):

# TODO Implement form and method populateform

    def populateform(self, cliente: Cliente):
        pass

    pass