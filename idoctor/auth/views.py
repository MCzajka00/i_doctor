from flask import flash, redirect, request, url_for, render_template
from flask_login import login_user, logout_user

from . import auth_bp
from .forms import LoginForm, SignUpForm
from .models import User
from .. import db


@auth_bp.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.get_by_username(form.username.data)
        if user is not None and user.check_password(form.password.data):
            login_user(user, form.remember_me.data)
            flash(f"Logged in as {user.username}")
            return redirect(request.args.get('next') or url_for("main.home"))
        flash("Incorrect username or password.")
    return render_template("login.html", form=form)


@auth_bp.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('main.home'))


@auth_bp.route('/signup', methods=["GET", "POST"])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        user_check = User.get_by_username(form.username.data)
        if user_check is None:
            user = User(username=form.username.data,
                        email=form.email.data,
                        password=form.password.data)

            db.session.add(user)
            db.session.commit()

            flash(f"Welcome, {user.username}! Please login!")
            return redirect(url_for('.login'))
        flash(f"Username or email is already used.")
    return render_template('signup.html', form=form)
