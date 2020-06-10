from datetime import datetime

from flask import Blueprint, flash, redirect, url_for, render_template

from idoctor import db
from idoctor.forms.visit_forms import VisitForm
from idoctor.models.doctor_models import Doctor
from idoctor.models.visit_models import Visit

visit_bp = Blueprint('visit', __name__, url_prefix='/visits')


@visit_bp.route('')
def visit_list():
    visits = [{
        "name": x.doctor.name,
        "tms": datetime.timestamp(x.start_visit)
    }
        for x in Visit.get_visit_all()]
    return render_template("visit.html", visits=visits)


@visit_bp.route('/add', methods=["GET", "POST"])
def visit_add():
    form = VisitForm()

    doctors = Doctor.get_doctors()
    list_of_doctors = [(0, '---')]
    for doctor in doctors:
        list_of_doctors.append((doctor.id, doctor.name))
    form.doctor.choices = list_of_doctors

    if form.validate_on_submit():
        start_visit = form.start_visit.data
        start_visit_hour = form.start_visit_hour.data
        doctor_id = form.doctor.data
        # TODO check if date is free

        new_visit = Visit(start_visit=datetime.combine(start_visit, start_visit_hour), doctor_id=doctor_id)
        db.session.add(new_visit)
        db.session.commit()

        flash(f'Your visit is reserved at {new_visit.start_visit} {start_visit_hour}')
        return redirect(url_for('main.home'))
    return render_template('visit_form.html', form=form, title='add visit')
