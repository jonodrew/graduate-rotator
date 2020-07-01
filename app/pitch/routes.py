from flask import render_template

from app.pitch import pitch_bp


@pitch_bp.route("/start", methods=["GET"])
def start():
    return render_template("pitch/start.html")
