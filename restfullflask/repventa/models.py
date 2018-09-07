from sqlalchemy import CheckConstraint
from restfullflask import db


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

    # One Repventas to many relationship
    # TODO Fix
    director = db.relationship('Repventa', backref='vendedores_vendedor',
                               remote_side=id_empleado,lazy=True)

    clientes = db.relationship('Cliente', backref='clientes_vendedor', lazy=True)

    pedidos = db.relationship('Pedido', backref='pedidos_vendedor', lazy=True)

    def handle_form(self, form):
        self.id_empleado = form.id_empleado.data
        self.nombre = form.nombre.data
        self.edad = form.edad.data

        if form.id_oficina.data == -1:
            pass

        else:
            self.id_oficina = form.id_oficina.data

        self.titulo = form.titulo.data
        self.contrato = form.contrato.data

        if form.id_director.data == -1:
            pass

        else:
            self.id_director = form.id_director.data

        self.cuota = form.cuota.data
        self.ventas = form.ventas.data

    def __repr__(self):
        return 'Empleado {} {}'.format(self.id_empleado,self.nombre)
