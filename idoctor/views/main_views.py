from flask import Blueprint, render_template

from idoctor import login_manager
from idoctor.auth.models import User

main_bp = Blueprint('main', __name__, url_prefix='/')


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@main_bp.route('/')
@main_bp.route('/home')
def home():
    return render_template('home.html')


@main_bp.errorhandler(403)
def forbidden(error):
    return "Forbidden"


@main_bp.errorhandler(404)
def not_found(error):
    return "Not found"


@main_bp.errorhandler(500)
def server_error(error):
    return "Server error"
