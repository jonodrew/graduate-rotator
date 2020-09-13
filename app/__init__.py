from flask import Flask
from config import Config


def create_app(configuration=Config):
    app = Flask(__name__, static_folder="static")

    app.config.from_object(configuration)

    from app.munkres_api import munkres_bp

    app.register_blueprint(munkres_bp, url_prefix="/munkres-api/v1/")

    from app.pitch import pitch_bp

    app.register_blueprint(pitch_bp, url_prefix="/pitch/")

    from app.main import main_bp

    app.register_blueprint(main_bp)

    return app
