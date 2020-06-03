from flask import Blueprint, flash, redirect, url_for, render_template

from idoctor import db
from idoctor.forms.visit_forms import VisitForm
from idoctor.models.visit_models import Visit

visit_bp = Blueprint('visit', __name__, url_prefix='/visits')


@visit_bp.route('/add', methods=["GET", "POST"])
def visit_add():
    form = VisitForm()

    if form.validate_on_submit():
        start_visit = form.start_visit.data
        doctor_id = 1

        # TODO check if date is free
        new_visit = Visit(start_visit=start_visit, doctor_id=doctor_id)
        db.session.add(new_visit)
        db.session.commit()

        flash(f'Your visit is reserved at {new_visit.start_visit}')
        return redirect(url_for('main.home'))
    return render_template('visit_form.html', form=form, title='add visit')
