from restfullflask import db
from sqlalchemy import CheckConstraint


class Producto(db.Model):
    id_fab = db.Column(db.String(3), primary_key=True)

    id_producto = db.Column(db.String(3), primary_key=True)

    descripcion = db.Column(db.TEXT, nullable=False)

    precio = db.Column(db.DECIMAL(precision=7, scale=2),
                       CheckConstraint('precio>0'), nullable=False)
    existencias = db.Column(db.INTEGER,
                            CheckConstraint('existencias>=0'), nullable=False)

    pedidos = db.relationship('Pedido', backref='pedidos_producto', lazy=True)

    """
        Instance model Producto from fields of form
        """

    def handle_form(self, form):
        self.id_fab = form.id_fab.data
        self.id_producto = form.id_producto.data
        self.descripcion = form.descripcion.data
        self.precio = form.precio.data
        self.existencias = form.existencias.data

    def __repr__(self):
        return 'Producto {} {}'.format(self.id_fab,self.id_producto)
