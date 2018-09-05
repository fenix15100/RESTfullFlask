from restfullflask.HelpersScripts.wtfhtml5 import IntegerField,DecimalField
from wtforms import Form, StringField, TextAreaField, validators, ValidationError
from restfullflask.producto.models import db,Producto


class ProductoForm(Form):
    id_fab = StringField('Cod.Fabricante', validators=[validators.Length(max=3,message="Como maximo 3 Caracteres alfanumericos"),validators.DataRequired("Introduce un Codigo de fabricante")])
    id_producto = StringField('Cod.Producto', validators=[validators.Length(max=3,message="Como maximo 3 Caracteres alfanumericos"),validators.DataRequired("Introduce un Codigo de Producto")])
    descripcion = TextAreaField('Descripcion',validators=[validators.DataRequired('Es necesaria una descripcion del producto')])
    precio= DecimalField('Precio',validators=[validators.DataRequired("Precio requerido")],places=2)
    existencias = IntegerField('Exsitencias',validators=[validators.DataRequired("Campo obligatorio")])

    #Set fields from a Model Producto

    def populateForm(self,Producto):

        self.id_fab.data=Producto.id_fab
        self.id_producto.data=Producto.id_producto
        self.descripcion.data=Producto.descripcion
        self.precio.data=Producto.precio
        self.existencias.data=Producto.existencias
