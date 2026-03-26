from flask import Blueprint, render_template, request, redirect, url_for, session
from app import db, bcrypt
from app.models import Instelling, Stage

main = Blueprint("main", __name__)

@main.route("/", methods=["GET", "POST"])
def homepage():
    instellingen = Instelling.query.all()

    if request.method == "POST":
        if not session.get("user_id"):
            return redirect("/login")
        
        user_id = session.get("user_id")

        existing_stage = Stage.query.filter(
            Stage.student_id == user_id,
            Stage.status.in_(["Aangemeld", "Geaccepteerd door bedrijf", "Begonnen"])
        ).first()

        if existing_stage:
            return "Je hebt al een actieve stage!"

        instelling_id = request.form.get("instelling_id")
        aantal_uren = request.form.get("instelling_totaal_uren")

        new_stage = Stage(
            student_id=user_id,
            instelling_id=instelling_id,
            status="Aangemeld",
            totaal_uren=aantal_uren,
        )

        db.session.add(new_stage)
        db.session.commit()

        return redirect("/")  

    return render_template("main.html", instellingen=instellingen)