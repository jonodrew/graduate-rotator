from flask import Blueprint

munkres_bp = Blueprint("munkres_api", __name__)

from app.munkres_api import routes  # noqa: E402,F401
