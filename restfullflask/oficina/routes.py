from flask import render_template, Blueprint, request, redirect, flash, url_for
from restfullflask.oficina.models import db, Oficina
from restfullflask.oficina.forms import OficinaForm

"""
Oficina BluePrint
"""

oficinaController = Blueprint('oficinaController', __name__, template_folder='templates/')


# Action (Get all entrys for a model "Oficina" and send array to template)
@oficinaController.route('/oficinas/', methods=['GET'])
def showAll():
    oficinas = db.session.query(Oficina).all()

    return render_template('oficina_list.html', oficinas=oficinas)


# Action (Add entry for a model "Oficina" and redirect to Action "ShowAll")
@oficinaController.route('/oficina/', methods=['GET', 'POST'])
def add():
    # Render a valid HTML5 form for handle data to Add a new entry "Oficina"
    form = OficinaForm(request.form)

    if request.method == 'POST' and form.validate():
        oficina = Oficina()
        oficina.handleForm(form)
        db.session.add(oficina)
        db.session.commit()
        flash('Oficina Added!')
        return redirect(url_for('oficinaController.showAll'))

    return render_template('oficina_add.html', form=form)


# Action (Edit one Entry for model "Oficina" and redirect to Action "ShowAll")
@oficinaController.route('/oficina/<int:id>/', methods=['GET', 'PUT'])
def edit(id):
    oficina = db.session.query(Oficina).get(id)
    form = OficinaForm(request.form)

    if request.method == b"PUT" and form.validate():
        oficina.handleForm(form)
        db.session.commit()
        flash('Oficina Updated!')
        return redirect(url_for('oficinaController.showAll'))

    # Set fields from a Model Oficina
    form.populateForm(oficina)

    return render_template('oficina_edit.html', form=form, id=id)


# Action (Delete one Entry for model "Oficina" and redirect to Action "ShowAll")
@oficinaController.route('/oficina/<int:id>/', methods=['DELETE'])
def delete(id):
    if request.method == b"DELETE":
        oficina = db.session.query(Oficina).get(id)
        db.session.delete(oficina)
        db.session.commit()
        flash('Oficina Deleted!')
        return redirect(url_for('oficinaController.showAll'))
