from flask import flash, redirect, request, url_for, render_template
from flask_login import login_user

from  . import auth_bp
from .forms import LoginForm
from .models import User


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

