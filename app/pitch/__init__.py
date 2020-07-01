from flask import Blueprint

pitch_bp = Blueprint("pitch", __name__)

from app.pitch import routes  # noqa: E402,F401
