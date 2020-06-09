from flask import Blueprint, redirect, url_for, render_template, flash, request
from flask_login import login_required

from idoctor import db
from idoctor.forms.clinic_forms import ClinicForm
from idoctor.models.clinic_models import Clinic

clinic_bp = Blueprint('clinic', __name__, url_prefix='/clinics')


@clinic_bp.route('/')
def clinics():
    return render_template('clinic_list.html', clinics=Clinic.get_clinics())


@clinic_bp.route('/add', methods=['GET', 'POST'])
@login_required
def clinic_add():
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


@clinic_bp.route('/edit/<int:clinic_id>', methods=['GET', 'POST'])
@login_required
def clinic_edit(clinic_id):
    clinic_for_edit = Clinic.query.filter_by(id=clinic_id).first_or_404()
    form = ClinicForm(obj=clinic_for_edit)

    if form.validate_on_submit():
        form.populate_obj(clinic_for_edit)
        db.session.commit()

        flash(f'{form.name.data} is edited successfully.')
        return redirect(url_for('clinic.clinics'))
    return render_template('clinic_form.html', form=form, title="Edit clinic")


@clinic_bp.route('/delete/<int:clinic_id>', methods=['GET', 'POST'])
@login_required
def clinic_delete(clinic_id):
    clinic_for_delete = Clinic.query.get_or_404(clinic_id)
    form = ClinicForm(obj=clinic_for_delete)

    if request.method == 'POST':
        db.session.delete(clinic_for_delete)
        db.session.commit()

        flash(f"Deleted {form.name.data} successfully.")
        return redirect(url_for('clinic.clinics'))
    else:
        flash(f"Please confirm deleting the clinic")
    return render_template('confirm_delete.html', clinic=clinics, nolinks=True)
