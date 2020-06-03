import os
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_datepicker import datepicker

# configure db
db = SQLAlchemy()
basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, 'dbs', 'idoctor.db')

# configure authentication
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


def create_app():
    idoctor = Flask(__name__)
    idoctor.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{db_path}"
    idoctor.config['SECRET_KEY'] = b'b\xad\x9e\xcc%""\xc2Yj(\x0e\xa5>\x16\x18'

    from idoctor.views.main_views import main_bp
    from idoctor.views.doctor_views import doctor_bp
    from idoctor.views.clinic_views import clinic_bp
    from idoctor.views.calendar_views import calendar_bp
    from idoctor.auth import auth_bp

    idoctor.register_blueprint(main_bp)
    idoctor.register_blueprint(doctor_bp)
    idoctor.register_blueprint(clinic_bp)
    idoctor.register_blueprint(calendar_bp)
    idoctor.register_blueprint(auth_bp)

    from idoctor.models.clinic_models import Clinic
    db.init_app(idoctor)
    login_manager.init_app(idoctor)
    Migrate(app=idoctor, db=db)

    Bootstrap(idoctor)
    datepicker(idoctor)

    return idoctor


app = create_app()
