from flask import Blueprint, render_template, request, redirect, url_for, session
from app import db, bcrypt
from app.models import Instelling, Stage, User

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

    if request.method == "POST":
        form_type = request.form.get("form_type")
        stage_id = request.form.get("stage_id")
        stage = Stage.query.get(stage_id)

        if not stage:
            return redirect("/beheer")

        if form_type == "start_stage":
            instelling = stage.instelling
            if instelling.aantal_studenten < instelling.max_aantal_studenten:
                stage.status = "Begonnen"
                instelling.aantal_studenten += 1
                db.session.commit()

        elif form_type == "stop_stage":
            if stage.status == "Begonnen":
                stage.status = "Afgerond"
                stage.instelling.aantal_studenten -= 1
                db.session.commit()

        return redirect("/beheer")

    stages = Stage.query.all()
    return render_template("accountpages/begeleiderProfile.html", stages=stages)


@profiles.route("/bedrijf-dashboard", methods=["GET", "POST"])
def bedrijfdashboardtpage():
    if not session.get("user_is_bedrijf_eigenaar"):
        return redirect("/")

    if request.method == "POST":
        stage_id = request.form.get("stage_id")
        stage = Stage.query.get(stage_id)

        if stage:
            stage.status = "Geaccepteerd door bedrijf"
            db.session.commit()

        return redirect("/bedrijf-dashboard")

    user_id = session.get("user_id")
    user = User.query.get(user_id)

    if not user or not user.bedrijf:
        return "Geen bedrijf gekoppeld aan dit account"

    stages = Stage.query.filter_by(instelling_id=user.bedrijf).all()

    return render_template("accountpages/eigenaarProfile.html", stages=stages)

