from flask_wtf import FlaskForm
from wtforms import SubmitField
from wtforms.fields.html5 import DateField, TimeField
from wtforms.validators import DataRequired


class VisitForm(FlaskForm):
    start_visit = DateField('Date', validators=[DataRequired()])
    start_visit_hour = TimeField('Time', validators=[DataRequired()])
    submit = SubmitField('Reserve')