from restfullflask import db
from sqlalchemy import CheckConstraint

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


    """
    Instance model Oficina from fields of form
    """
    def handleForm(self,form):
        self.ciudad = form.ciudad.data
        self.region = form.region.data
        self.director = form.director.data
        self.objetivo = form.objetivo.data
        self.ventas = form.ventas.data

    """
    Represent object in String Format
    """

    def __repr__(self):
        return '<Oficina %r>' % self.id_oficina + "_" + self.ciudad + "_" + self.region