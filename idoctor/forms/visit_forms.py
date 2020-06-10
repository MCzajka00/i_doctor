from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField
from wtforms.fields.html5 import DateField, TimeField
from wtforms.validators import DataRequired


class VisitForm(FlaskForm):
    start_visit = DateField('Date', validators=[DataRequired()])
    start_visit_hour = TimeField('Time', validators=[DataRequired()])
    clinic = SelectField("Choose the clinic", coerce=int, choices=[(1, '---'), (2, 'szpital'), (3, 'przychodnia')])
    doctor = SelectField("Choose the doctor", coerce=int)
    submit = SubmitField('Reserve')