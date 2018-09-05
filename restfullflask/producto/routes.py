from flask import render_template,Blueprint,request,redirect,flash,url_for
from sqlalchemy.exc import IntegrityError

from restfullflask.producto.models import db,Producto
from restfullflask.producto.forms import ProductoForm

"""
Producto BluePrint
"""

productoController = Blueprint('productoController', __name__,template_folder='templates/')



@productoController.route('/productos/',methods=['GET'])
def showAll():
    productos = db.session.query(Producto).all()

    return render_template('producto_list.html', productos=productos)



@productoController.route('/producto/',methods=['GET','POST'])
def add():

    form = ProductoForm(request.form)


    if request.method == 'POST' and form.validate():

        producto = Producto()
        producto.handleForm(form)
        try:
            db.session.add(producto)
            db.session.commit()
            flash('Producto Added!')
            return redirect(url_for('productoController.showAll'))
        except IntegrityError:
            db.session.rollback()
            form.id_fab.errors.append("Ya hay un producto con la misma combinacion de Codigo de Fabricante y Codigo de Producto")


    return render_template('producto_add.html', form=form)


@productoController.route('/producto/<string:id_fab>/<string:id_producto>/',methods=['GET','PUT'])
def edit(id_fab,id_producto):

    producto=db.session.query(Producto).filter_by(id_fab=id_fab,id_producto=id_producto).first()
    form = ProductoForm(request.form)

    if request.method==b"PUT" and form.validate():

        producto.handleForm(form)
        try:
            db.session.commit()
            flash('Producto Updated!')
            return redirect(url_for('productoController.showAll'))
        except IntegrityError:
            db.session.rollback()
            form.id_fab.errors.append("Ya hay un producto con la misma combinacion de Codigo de Fabricante y Codigo de Producto")


    form.populateForm(producto)

    return render_template('producto_edit.html', form=form, id_fab=id_fab, id_producto=id_producto)


@productoController.route('/oficina/<string:id_fab>/<string:id_producto>/',methods=['DELETE'])
def delete(id_fab,id_producto):

    if request.method == b"DELETE":

        producto = db.session.query(Producto).filter_by(id_fab=id_fab,id_producto=id_producto).first()
        db.session.delete(producto)
        db.session.commit()
        flash('Producto Deleted!')
        return redirect(url_for('productoController.showAll'))