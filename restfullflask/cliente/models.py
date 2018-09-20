
from sqlalchemy import CheckConstraint

from restfullflask import db

class Cliente(db.Model):
    id_cliente = db.Column(db.INTEGER, primary_key=True)

    empresa = db.Column(db.String(20), nullable=False)

    id_vendedor = db.Column(db.INTEGER,
                            db.ForeignKey('repventa.id_empleado',
                                          ondelete="RESTRICT", onupdate="CASCADE"), nullable=False)

    limite_credito = db.Column(db.DECIMAL(precision=8, scale=2),
                               CheckConstraint('limite_credito>0 and limite_credito<120000'))

    pedidos = db.relationship('Pedido', backref='clientes_pedido', lazy=True)

    def __repr__(self):
        return '<cliente %r>' % self.id_cliente + "_" + self.empresa

    """
        Instance model Cliente from fields of form
    """

    def handle_form(self, form):
        pass
    # TODO implement method