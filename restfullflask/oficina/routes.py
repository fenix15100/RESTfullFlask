from flask import render_template, Blueprint, request, redirect, flash, url_for
from restfullflask.oficina.models import db, Oficina
from restfullflask.oficina.forms import OficinaForm

"""
Oficina BluePrint
"""

oficinaController = Blueprint('oficinaController', __name__, template_folder='templates/')


# Action (Get all entrys for a model "Oficina" and send array to template)
@oficinaController.route('/oficinas/', methods=['GET'])
def show_all():
    oficinas = db.session.query(Oficina).all()

    return render_template('oficina_list.html', oficinas=oficinas)


# Action (Add entry for a model "Oficina" and redirect to Action "ShowAll")
@oficinaController.route('/oficina/', methods=['GET', 'POST'])
def add():
    # Render a valid HTML5 form for handle data to Add a new entry "Oficina"
    form = OficinaForm(request.form)

    if request.method == 'POST' and form.validate():
        oficina = Oficina()
        oficina.handle_form(form)
        db.session.add(oficina)
        db.session.commit()
        flash('Oficina Added!')
        return redirect(url_for('oficinaController.show_all'))

    return render_template('oficina_add.html', form=form)


# Action (Edit one Entry for model "Oficina" and redirect to Action "ShowAll")
@oficinaController.route('/oficina/<id_oficina>/', methods=['GET', 'PUT'])
def edit(id_oficina):
    oficina = db.session.query(Oficina).get(id_oficina)
    form = OficinaForm(request.form)

    if request.method == b"PUT" and form.validate():
        oficina.handle_form(form)
        db.session.commit()
        flash('Oficina Updated!')
        return redirect(url_for('oficinaController.show_all'))

    # Set fields from a Model Oficina
    form.populateform(oficina)

    return render_template('oficina_edit.html', form=form, id_oficina=id_oficina)


# Action (Delete one Entry for model "Oficina" and redirect to Action "ShowAll")
@oficinaController.route('/oficina/<id_oficina>/', methods=['DELETE'])
def delete(id_oficina):
    if request.method == b"DELETE":
        oficina = db.session.query(Oficina).get(id_oficina)
        db.session.delete(oficina)
        db.session.commit()
        flash('Oficina Deleted!')
        return redirect(url_for('oficinaController.show_all'))
