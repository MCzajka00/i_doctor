from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Regexp, EqualTo, Email, ValidationError

from idoctor.auth.models import User


class LoginForm(FlaskForm):
    username = StringField('Your username:', validators=[DataRequired()])
    password = PasswordField('Password:', validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log in')


class SignUpForm(FlaskForm):
    username = StringField('Username:',
                           validators=[
                               DataRequired(),
                               Length(3, 80),
                               Regexp('^[A-Za-z0-9_]{3,}$',
                                      message="Username consist of numbers, letters and underscores")
                           ])
    password = PasswordField('Password:',
                             validators=[
                                 DataRequired(),
                                 EqualTo('password2',
                                         message='Password must match')
                             ])
    password2 = PasswordField('Confirm password:',
                              validators=[
                                  DataRequired()
                              ])
    email = StringField('Email',
                        validators=[
                            DataRequired(),
                            Length(5, 120),
                            Email()
                        ])
    submit = SubmitField('Sign up')

    def validate_email(self, email_field):
        if User.query.filter_by(email=email_field.data).first():
            raise ValidationError('There is already user with this e-mail.')

    def validate_username(self, username_field):
        if User.query.filter_by(username=username_field.data).first():
            raise ValidationError('This username is already taken.')
