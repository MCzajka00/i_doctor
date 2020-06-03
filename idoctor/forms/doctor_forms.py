from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length


class DoctorForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=3, max=30)])
    specialization =StringField('Specialization', validators=[DataRequired(), Length(min=3, max=100)])
    submit = SubmitField('Add doctor')


class DoctorEditForm(DoctorForm):
    submit = SubmitField('Edit')


class DoctorDeleteForm(FlaskForm):
    submit = SubmitField('Delete')


class DoctorSearchForm(FlaskForm):
    search = StringField('Find')
    submit = SubmitField('Search')