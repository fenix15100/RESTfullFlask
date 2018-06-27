from sqlalchemy import CheckConstraint
from sqlalchemy.orm import relationship

from app import db

class Producto(db.Model):
    id_fab = db.Column(db.String(3), primary_key=True)

    id_producto = db.Column(db.String(3), primary_key=True)

    descripcion=db.Column(db.TEXT,nullable=False)

    precio=db.Column(db.DECIMAL(precision=7,scale=2),
                     CheckConstraint('precio>0'),nullable=False)
    existencias=db.Column(db.INTEGER,
                          CheckConstraint('existencias>=0'),nullable=False)

    def __repr__(self):
        return '<Producto %r>' % self.id_fab+"_"+self.id_producto

class Oficina (db.Model):

    id_oficina=db.Column(db.INTEGER,primary_key=True)

    ciudad=db.Column(db.String(15),nullable=False)

    region=db.Column(db.String(10),nullable=False)

    director=db.Column(db.INTEGER)

    objetivo=db.Column(db.DECIMAL(precision=9,scale=2),
                       CheckConstraint('objetivo>=0'))

    ventas=db.Column(db.DECIMAL(precision=9,scale=2),
                     CheckConstraint('ventas>=0'),nullable=False)

    repventas=db.relationship('repventa', backref='id_oficina', lazy=True)

    def __repr__(self):
        return '<Oficina %r>' % self.id_oficina+"_"+self.ciudad+"_"+self.region


class Repventa(db.Model):

    id_empleado=db.Column(db.INTEGER,primary_key=True)

    nombre=db.Column(db.String(15),nullable=False)

    edad=db.Column(db.INTEGER,CheckConstraint('edad>18'))

    id_oficina=db.Column(db.INTEGER,
                         db.ForeignKey('oficina.id_oficina',
                                       ondelete="SET NULL",onupdate="CASCADE"))

    titulo=db.Column(db.String(10))

    contrato=db.Column(db.DATE,
                       CheckConstraint('contrato<=current_timestamp'),nullable=False)

    id_director=db.Column(db.INTEGER,
                          db.ForeignKey("repventa.id_empleado",
                                        ondelete="RESTRICT",onupdate="CASCADE"))

    cuota=db.Column(db.DECIMAL(precision=8,scale=2),
                    CheckConstraint('cuota>=0'))

    ventas = db.Column(db.DECIMAL(precision=8, scale=2),
                       CheckConstraint('ventas>=0'),nullable=False)

    director = db.relationship('repventa', backref='subordinados',
                                    remote_side=id_empleado)

    clientes = db.relationship('cliente', backref='id_cliente', lazy=True)

    def __repr__(self):
        return '<Empleado %r>' % self.id_empleado+"_"+self.nombre



class Cliente(db.Model):

  pass

#TODO Acabar Modelo Cliente y Pedidos
#TODO Buscar un vendor compatible con el ORM para que CRUDEE los modelos
#TODO Añadir soporte de autententificacion Hasheada a nivel de Base de datos

