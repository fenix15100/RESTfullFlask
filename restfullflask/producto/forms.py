from restfullflask.HelpersScripts.wtfhtml5 import IntegerField, DecimalField
from wtforms import Form, StringField, TextAreaField, validators
from restfullflask.producto.models import Producto


class ProductoForm(Form):

    id_fab = StringField('Cod.Fabricante',
                         validators=[validators.Length(max=3, message="Como maximo 3 Caracteres alfanumericos"),
                                     validators.InputRequired("Introduce un Codigo de fabricante")])

    id_producto = StringField('Cod.Producto',
                              validators=[validators.Length(max=3, message="Como maximo 3 Caracteres alfanumericos"),
                                          validators.InputRequired("Introduce un Codigo de Producto")])

    descripcion = TextAreaField('Descripcion',
                                validators=[validators.InputRequired('Es necesaria una descripcion del producto')])

    precio = DecimalField('Precio',
                          validators=[validators.InputRequired("Precio requerido"), validators.NumberRange(min=1)],
                          places=2)

    existencias = IntegerField('Exsitencias', validators=[validators.InputRequired("Campo obligatorio"),
                                                          validators.NumberRange(min=0,
                                                                                 message="La existencias no pueden "
                                                                                         "ser inferior a 0")])

    # Set fields from a Model Producto

    def populateform(self, producto: Producto):
        self.id_fab.data = producto.id_fab
        self.id_producto.data = producto.id_producto
        self.descripcion.data = producto.descripcion
        self.precio.data = producto.precio
        self.existencias.data = producto.existencias
