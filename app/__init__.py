from flask import Flask
from config import Config


def create_app(configuration=Config):
    app = Flask(__name__)

    app.config.from_object(configuration)

    from app.munkres_api import munkres_bp

    app.register_blueprint(munkres_bp, url_prefix="/munkres-api/v1/")

    return app
