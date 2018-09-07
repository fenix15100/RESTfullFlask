from flask import render_template, Blueprint, request, redirect, flash, url_for
from sqlalchemy.exc import IntegrityError

from restfullflask.repventa.models import db, Repventa
from restfullflask.repventa.forms import RepventaForm


"""
Repventa BluePrint
"""

repventaController = Blueprint('repventaController', __name__, template_folder='templates/')

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
            return redirect(url_for('oficinaController.show_all'))

        except IntegrityError as e:
            db.session.rollback()
            flash(e)

    return render_template('repventa_add.html', form=form)
