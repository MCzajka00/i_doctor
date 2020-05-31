from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.fields.html5 import DateField


class CalendarForm(FlaskForm):
    date = StringField('Pick date')
    submit = SubmitField('Submit')