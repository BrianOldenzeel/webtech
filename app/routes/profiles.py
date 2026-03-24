from flask import Blueprint, render_template, request, redirect, url_for, session
from app import db, bcrypt
from app.models import Instelling, Stage

profiles = Blueprint("profiles", __name__)

@profiles.route("/profile", methods=["GET", "POST"])
def profilepage():
    if not session.get("user_is_student"):
        return redirect("/")

    stages = Stage.query.filter_by(student_id=session.get("user_id")).all()

    return render_template("accountpages/profile.html", stages=stages)

@profiles.route("/beheer", methods=["GET", "POST"])
def beheerpage():
    if not session.get("user_is_begeleider"):
        return redirect("/")

    stages = Stage.query.all()
    return render_template("accountpages/begeleiderProfile.html", stages=stages)

