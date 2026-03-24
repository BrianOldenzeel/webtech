from flask import Blueprint, render_template, request, redirect, url_for, session
from app import db, bcrypt
from app.models import User

auth = Blueprint("auth", __name__)

@auth.route("/login", methods=["GET", "POST"])
def loginpage():
    return render_template("auth/login.html")

@auth.route("/register", methods=["GET", "POST"])
def registerpage():
    if request.method == "POST":
        voornaam = request.form.get("voornaam")
        achternaam = request.form.get("achternaam")
        email = request.form.get("email")
        password = request.form.get("password")
        studie = request.form.get("studie")

        hashedPW = bcrypt.generate_password_hash(password).decode("utf-8")

        new_user = User(
            voornaam=voornaam,
            achternaam=achternaam,
            email=email,
            password = hashedPW,
            studie=studie
        )

        db.session.add(new_user)
        db.session.commit()

        return redirect("/login")

    return render_template("auth/register.html")