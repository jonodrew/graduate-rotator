from flask import render_template

from app.pitch import pitch_bp


@pitch_bp.route("/start", methods=["GET"])
def start():
    return render_template("pitch/start.html")


@pitch_bp.route("/the-problem", methods=["GET"])
def problem():
    return render_template("pitch/the-problem.html")
