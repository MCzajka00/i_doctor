import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, 'dbs', 'idoctor.db')


def create_app():
    idoctor = Flask(__name__)
    idoctor.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{db_path}"
    idoctor.config['SECRET_KEY'] = b'b\xad\x9e\xcc%""\xc2Yj(\x0e\xa5>\x16\x18'

    from idoctor.views.main_views import main_bp

    idoctor.register_blueprint(main_bp)

    db.init_app(idoctor)
    migrate = Migrate(app=idoctor, db=db)

    return idoctor


app = create_app()
