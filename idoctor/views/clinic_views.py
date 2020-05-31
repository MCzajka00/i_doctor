from flask import Blueprint, redirect, url_for, render_template, flash

from idoctor import db
from idoctor.forms.clinic_forms import ClinicForm
from idoctor.models.clinic_models import Clinic

clinic_bp = Blueprint('clinic', __name__, url_prefix='/clinics')


@clinic_bp.route('/')
def clinics():
    return render_template('clinic_list.html', clinics=Clinic.get_clinics())


# TODO add login required
# TODO change function name clinic => clinic_add
@clinic_bp.route('/add', methods=['GET', 'POST'])
def clinic():
    form = ClinicForm()

    if form.validate_on_submit():
        name = form.name.data
        address = form.address.data

        new_clinic = Clinic(name=name, address=address)
        db.session.add(new_clinic)
        db.session.commit()

        flash(f'{name} is added successfully.')
        return redirect(url_for('main.home'))
    return render_template('clinic_form.html', form=form, title="Add clinic")


# TODO add login required
@clinic_bp.route('/edit/<int:clinic_id>', methods=['GET', 'POST'])
def clinic_edit(clinic_id):
    clinic_for_edit = Clinic.query.filter_by(id=clinic_id).first_or_404()
    form = ClinicForm(obj=clinic_for_edit)

    if form.validate_on_submit():
        form.populate_obj(clinic_for_edit)
        db.session.commit()

        flash(f'{form.name.data} is edited successfully.')
        return redirect(url_for('clinic.clinics'))
    return render_template('clinic_form.html', form=form, title="Edit clinic")


# TODO implement delete for clinic (login required)
@clinic_bp.route('/delete/<int:clinic_id>')
def clinic_delete(clinic_id):
    pass
