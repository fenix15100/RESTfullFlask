from flask import render_template, Blueprint, request, redirect, flash, url_for
from sqlalchemy.exc import IntegrityError

from restfullflask.repventa.models import db, Repventa
from restfullflask.repventa.forms import RepventaForm


"""
Repventa BluePrint
"""

repventaController = Blueprint('repventaController', __name__, template_folder='templates/')


@repventaController.route('/repventas/', methods=['GET'])
def show_all():
    repventas = db.session.query(Repventa).all()

    return render_template('repventa_list.html', repventas=repventas)


@repventaController.route('/repventa/', methods=['GET', 'POST'])
def add():

    form = RepventaForm(request.form)

    if request.method == 'POST' and form.validate():
        repventa = Repventa()
        repventa.handle_form(form)

        try:
            db.session.add(repventa)
            db.session.commit()
            flash('Repventa Added!')
            return redirect(url_for('repventaController.show_all'))

        except IntegrityError as e:
            db.session.rollback()
            flash(e)

    return render_template('repventa_add.html', form=form)


@repventaController.route('/repventa/<int:id_empleado>', methods=['GET', 'PUT'])
def edit(id_empleado):
    repventa = db.session.query(Repventa).get(id_empleado)
    form = RepventaForm(request.form)

    if request.method == b"PUT" and form.validate():

        repventa.handle_form(form)
        try:

            db.session.commit()
            flash('Repventa Updated!')
            return redirect(url_for('repventaController.show_all'))
        except IntegrityError as e:
            db.session.rollback()
            flash(e)


    form.populateform(repventa)

    return render_template('repventa_edit.html', form=form, id_empleado=id_empleado)


@repventaController.route('/repventa/<int:id_empleado>', methods=['DELETE'])
def delete(id_empleado):
    if request.method == b"DELETE":
        repventa = db.session.query(Repventa).get(id_empleado)

        try:
            try:
                if repventa.isdirector():
                    raise ValueError(
                        "Violada Clave Ajena: fk_repventas_director_repventas ON DELETE RESTRICT ON UPDATE CASCADE")
            except ValueError as e:
                db.session.rollback()
                flash(repr(e.args))
                return redirect(url_for('repventaController.show_all'))

            db.session.delete(repventa)
            db.session.commit()
            flash('Repventa Deleted!')
        except IntegrityError as e:
            db.session.rollback()
            flash(e)

        return redirect(url_for('repventaController.show_all'))