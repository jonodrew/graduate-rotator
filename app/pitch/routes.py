from flask import render_template, session
from app.pitch import pitch_bp
from random import randrange


@pitch_bp.route("/start", methods=["GET"])
def start():
    return render_template("pitch/start.html")


@pitch_bp.route("/the-problem", methods=["GET"])
def problem():
    return render_template("pitch/the-problem.html")


@pitch_bp.route("/the-approach", methods=["GET"])
def approach():
    semi_random_data = [[randrange(0, 25) for i in range(10)] for j in range(10)]
    session["matrix"] = semi_random_data
    return render_template("pitch/the-approach.html", data=semi_random_data)
