from restfullflask.HelpersScripts.wtfhtml5 import IntegerField,DecimalField
from wtforms import Form, StringField, TextAreaField, validators


class ProductoForm(Form):
    id_fab = StringField('Cod.Fabricante', validators=[validators.Length(max=3,message="Como maximo 3 Caracteres alfanumericos"),validators.DataRequired("Introduce un Codigo de fabricante")])
    id_producto = StringField('Cod.Producto', validators=[validators.Length(max=3,message="Como maximo 3 Caracteres alfanumericos"),validators.DataRequired("Introduce un Codigo de Producto")])
    descripcion = TextAreaField('Descripcion',validators=[validators.DataRequired('Es necesaria una descripcion del producto')])
    precio= DecimalField('Precio',validators=[validators.DataRequired("Precio requerido"),validators.NumberRange(min=1)],places=2)
    existencias = IntegerField('Exsitencias',validators=[validators.DataRequired("Campo obligatorio"),validators.NumberRange(min=0,message="La existencias no pueden ser inferior a 0")])

    #Set fields from a Model Producto

    def populateForm(self,Producto):

        self.id_fab.data=Producto.id_fab
        self.id_producto.data=Producto.id_producto
        self.descripcion.data=Producto.descripcion
        self.precio.data=Producto.precio
        self.existencias.data=Producto.existencias
