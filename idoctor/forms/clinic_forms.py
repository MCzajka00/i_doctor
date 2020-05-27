from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length


class ClinicForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=3, max=30)])
    address = TextAreaField('Address', validators=[DataRequired(), Length(min=3, max=100)])
    submit = SubmitField('Add clinic')