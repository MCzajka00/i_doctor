from flask import Blueprint, redirect, url_for, render_template, flash, request
from flask_login import login_required

from idoctor import db
from idoctor.forms.doctor_forms import DoctorForm, DoctorEditForm, DoctorSearchForm, DoctorDeleteForm
from idoctor.models.doctor_models import Doctor

doctor_bp = Blueprint('doctor', __name__, url_prefix='/doctors')


@doctor_bp.route('/', methods=["GET"])
def doctors():
    form = DoctorSearchForm(search=request.args.get('search'), meta={"csrf": False})
    form_delete = DoctorDeleteForm()
    if form.validate() and request.args.get('search') is not None:
        doctor_results = Doctor.query.filter(Doctor.name.like(f"%{request.args.get('search')}%")).all()
        res = [{"id": c.id, "name": c.name, "specialization": c.specialization} for c in doctor_results]
    else:
        res = Doctor.get_doctors()
    return render_template('doctor_list.html', form=form, doctors=res, form_delete=form_delete)


@doctor_bp.route('/add', methods=['GET', 'POST'])
@login_required
def doctor_add():
    form = DoctorForm()

    if form.validate_on_submit():
        name = form.name.data
        specialization = form.specialization.data
        duration_visit = form.duration_visit.data

        new_doctor = Doctor(name=name, specialization=specialization, duration_visit=duration_visit)
        db.session.add(new_doctor)
        db.session.commit()

        flash(f'{name} is added successfully.')
        return redirect(url_for('main.home'))
    return render_template('doctor_form.html', form=form, title="Add doctor")


@doctor_bp.route('/edit/<int:doctor_id>', methods=['GET', 'POST'])
@login_required
def doctor_edit(doctor_id):
    doctor_for_edit = Doctor.query.filter_by(id=doctor_id).first_or_404()
    form = DoctorEditForm(obj=doctor_for_edit)

    if form.validate_on_submit():
        form.populate_obj(doctor_for_edit)
        db.session.commit()

        flash(f'{form.name.data} is edited successfully.')
        return redirect(url_for('doctor.doctors'))
    return render_template('doctor_form.html', form=form, title="Edit doctor")


@doctor_bp.route('/delete/<int:doctor_id>', methods=['POST'])
@login_required
def doctor_delete(doctor_id):
    doctor_for_delete = Doctor.query.get_or_404(doctor_id)
    db.session.delete(doctor_for_delete)
    db.session.commit()

    flash(f"Deleted {doctor_for_delete.name} successfully.")
    return redirect(url_for('.doctors'))
