from sqlalchemy import CheckConstraint
from app import db

class Products(db.Model):
    id_fab = db.Column(db.String(3), primary_key=True)
    id_producto = db.Column(db.String(3), primary_key=True)
    descripcion=db.Column(db.TEXT,nullable=False)
    precio=db.Column(db.DECIMAL(precision=7,scale=2),CheckConstraint('precio>0'),nullable=False)
    existencias=db.Column(db.INTEGER,CheckConstraint('existencias>=0'),nullable=False)

    def __repr__(self):
        return '<Producto %r>' % self.id_fab+"_"+self.id_producto



