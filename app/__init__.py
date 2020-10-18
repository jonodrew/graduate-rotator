from flask import Flask
from config import Config


def create_app(configuration=Config):
    app = Flask(__name__, static_folder="static")

    from app.models import db, migrate

    app.config.from_object(configuration)
    db.init_app(app)
    migrate.init_app(app, db)

    from app.munkres_api import munkres_bp

    app.register_blueprint(munkres_bp, url_prefix="/munkres-api/v1/")

    from app.pitch import pitch_bp

    app.register_blueprint(pitch_bp, url_prefix="/pitch/")

    from app.main import main_bp

    app.register_blueprint(main_bp)

    from app.profile import profile_bp

    app.register_blueprint(profile_bp, url_prefix="/profile/")

    return app
