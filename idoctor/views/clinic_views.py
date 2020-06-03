from flask import Blueprint, redirect, url_for, render_template, flash, request
from flask_login import login_required

from idoctor import db
from idoctor.forms.clinic_forms import ClinicForm, ClinicEditForm, ClinicSearchForm, ClinicDeleteForm
from idoctor.models.clinic_models import Clinic

clinic_bp = Blueprint('clinic', __name__, url_prefix='/clinics')


@clinic_bp.route('/', methods=["GET"])
def clinics():
    form = ClinicSearchForm(search=request.args.get('search'), meta={"csrf": False})
    form_delete = ClinicDeleteForm()
    res = Clinic.get_clinics()
    if form.validate() and request.args.get('search') is not None:
        clinic_results = Clinic.query.filter(Clinic.name.like(f"%{request.args.get('search')}%")).all()
        res = [{"id": c.id, "name": c.name, "address": c.address} for c in clinic_results]
    return render_template('clinic_list.html', form=form, clinics=res, form_delete=form_delete)


# TODO change function name clinic => clinic_add
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
    form = ClinicEditForm(obj=clinic_for_edit)

    if form.validate_on_submit():
        form.populate_obj(clinic_for_edit)
        db.session.commit()

        flash(f'{form.name.data} is edited successfully.')
        return redirect(url_for('clinic.clinics'))
    return render_template('clinic_form.html', form=form, title="Edit clinic")


# TODO implement delete for clinic
@clinic_bp.route('/delete/<int:clinic_id>', methods=['POST'])
@login_required
def clinic_delete(clinic_id):
    clinic_for_delete = Clinic.query.get_or_404(clinic_id)
    db.session.delete(clinic_for_delete)
    db.session.commit()

    flash(f"Deleted {clinic_for_delete.name} successfully.")
    return redirect(url_for('.clinics'))
