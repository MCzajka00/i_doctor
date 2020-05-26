from flask import Flask


def create_app():
    idoctor = Flask(__name__)

    from idoctor.views.main_views import main_bp

    idoctor.register_blueprint(main_bp)

    return idoctor


app = create_app()


