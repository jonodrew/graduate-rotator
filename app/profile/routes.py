from flask import render_template
from app.profile import profile_bp


@profile_bp.route("/index", methods=["GET"])
def index():
    content = {
        "history": [
            {
                "id": 1,
                "title": "Finance manager",
                "anchor": "Finance",
                "evaluation": "Met",
            },
            {
                "id": 2,
                "title": "Assistant Product Manager",
                "anchor": "Digital",
                "evaluation": "Exceeded",
            },
        ],
        "candidate": {
            "first_name": "Antonia",
            "last_name": "Ivanovna",
            "specialism": "Property",
        },
    }

    return render_template("profile/profile.html", **content)
