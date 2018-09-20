"""
This module contains all models used by application
If need more information related to declaring models go here
http://flask-sqlalchemy.pocoo.org/2.3/models/#one-to-many-relationships
http://docs.sqlalchemy.org/en/latest/orm/
"""

from sqlalchemy import CheckConstraint,ForeignKeyConstraint

from restfullflask import db



# FIXME refactor backref en todos los modelos para que tengan nombres coherentes

class Pedido(db.Model):
    id_pedido = db.Column(db.INTEGER, primary_key=True)

    fecha_pedido = db.Column(db.DATE,
                             CheckConstraint('fecha_pedido<=current_timestamp'),
                             nullable=False)

    id_cliente = db.Column(db.INTEGER,
                           db.ForeignKey('cliente.id_cliente',
                                         ondelete="RESTRICT", onupdate="CASCADE"), nullable=False)
    id_vendedor = db.Column(db.INTEGER,
                            db.ForeignKey('repventa.id_empleado',
                                          ondelete="SET NULL", onupdate="CASCADE"))
    id_fab = db.Column(db.String(3), nullable=False)

    id_producto = db.Column(db.String(3), nullable=False)

    cantidad= db.Column(db.Integer,
                        CheckConstraint('cantidad<0 or cantidad>0'), nullable=False)

    importe = db.Column(db.DECIMAL(precision=7 , scale=2),
                         CheckConstraint('importe<0 or importe>0'), nullable=False)

    __table_args__ = (ForeignKeyConstraint(('id_fab','id_producto'),
                                           ['producto.id_fab', 'producto.id_producto'],ondelete="RESTRICT",onupdate="CASCADE"),
                      {})


    def __repr__(self):
        return '<Pedido %r>' % self.id_pedido + "_" + self.fecha_pedido

