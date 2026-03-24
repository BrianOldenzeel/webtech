from flask import Blueprint, render_template, request, redirect, url_for, session
from app import db, bcrypt
from app.models import User

auth = Blueprint("auth", __name__)

@auth.route("/login", methods=["GET", "POST"])
def loginpage():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()

        if user and bcrypt.check_password_hash(user.password, password):
            session["user_id"] = user.id
            session["user_voornaam"] = user.voornaam
            session["user_is_student"] = user.is_student
            session["user_is_begeleider"] = user.is_begeleider
            session["user_is_bedrijf_eigenaar"] = user.is_bedrijf_eigenaar
            return redirect("/")

        return "Fout tijdens het inloggen"    

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
            studie=studie,
            is_student=True
        )

        db.session.add(new_user)
        db.session.commit()

        return redirect("/login")

    return render_template("auth/register.html")


@auth.route("/logout")
def logout():
    session.clear()
    return redirect("/")