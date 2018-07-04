#This module contains all models used by application
#If need more information related to declaring models go here
#http://flask-sqlalchemy.pocoo.org/2.3/models/#one-to-many-relationships
#http://docs.sqlalchemy.org/en/latest/orm/

from sqlalchemy import CheckConstraint,ForeignKeyConstraint

from restfullflask import db


class Producto(db.Model):
    id_fab = db.Column(db.String(3), primary_key=True)

    id_producto = db.Column(db.String(3), primary_key=True)

    descripcion = db.Column(db.TEXT, nullable=False)

    precio = db.Column(db.DECIMAL(precision=7, scale=2),
                       CheckConstraint('precio>0'), nullable=False)
    existencias = db.Column(db.INTEGER,
                            CheckConstraint('existencias>=0'), nullable=False)

    pedidos = db.relationship('Pedido', backref='pedidos_producto', lazy=True)

    def __repr__(self):
        return '<Producto %r>' % self.id_fab + "_" + self.id_producto


class Oficina(db.Model):
    id_oficina = db.Column(db.INTEGER, primary_key=True)

    ciudad = db.Column(db.String(15), nullable=False)

    region = db.Column(db.String(10), nullable=False)

    director = db.Column(db.INTEGER)

    objetivo = db.Column(db.DECIMAL(precision=9, scale=2),
                         CheckConstraint('objetivo>=0'))

    ventas = db.Column(db.DECIMAL(precision=9, scale=2),
                       CheckConstraint('ventas>=0'), nullable=False)

    repventas = db.relationship('Repventa', backref='repventas_oficina', lazy=True)

    def __init__(self,ciudad,region,director,objetivo,ventas):
        self.ciudad=ciudad
        self.region=region
        self.director=director
        self.objetivo=objetivo
        self.ventas=ventas


    def __repr__(self):
        return '<Oficina %r>' % self.id_oficina + "_" + self.ciudad + "_" + self.region


class Repventa(db.Model):
    id_empleado = db.Column(db.INTEGER, primary_key=True)

    nombre = db.Column(db.String(15), nullable=False)

    edad = db.Column(db.INTEGER, CheckConstraint('edad>18'))

    id_oficina = db.Column(db.INTEGER,
                           db.ForeignKey('oficina.id_oficina',
                                         ondelete="SET NULL", onupdate="CASCADE"))

    titulo = db.Column(db.String(10))

    contrato = db.Column(db.DATE,
                         CheckConstraint('contrato<=current_timestamp'), nullable=False)

    id_director = db.Column(db.INTEGER,
                            db.ForeignKey("repventa.id_empleado",
                                          ondelete="RESTRICT", onupdate="CASCADE"))

    cuota = db.Column(db.DECIMAL(precision=8, scale=2),
                      CheckConstraint('cuota>=0'))

    ventas = db.Column(db.DECIMAL(precision=8, scale=2),
                       CheckConstraint('ventas>=0'), nullable=False)

    director = db.relationship('Repventa', backref='subordinados',
                               remote_side=id_empleado)

    clientes = db.relationship('Cliente', backref='clientes_vendedor', lazy=True)

    pedidos = db.relationship('Pedido', backref='pedidos_vendedor', lazy=True)

    def __repr__(self):
        return '<Empleado %r>' % self.id_empleado + "_" + self.nombre


class Cliente(db.Model):
    id_cliente = db.Column(db.INTEGER, primary_key=True)

    empresa = db.Column(db.String(20), nullable=False)

    id_vendedor = db.Column(db.INTEGER,
                            db.ForeignKey('repventa.id_empleado',
                                          ondelete="RESTRICT", onupdate="CASCADE"), nullable=False)

    limite_credito = db.Column(db.DECIMAL(precision=8, scale=2),
                               CheckConstraint('limite_credito>0 and limite_credito<120000'))

    pedidos = db.relationship('Pedido', backref='pedidos_cliente', lazy=True)

    def __repr__(self):
        return '<Cliente %r>' % self.id_cliente + "_" + self.empresa


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

