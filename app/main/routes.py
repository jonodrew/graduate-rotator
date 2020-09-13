from flask import render_template
from app.main import main_bp


@main_bp.route("/weighting", methods=["GET"])
def weighting():
    return render_template("weighting.html")
