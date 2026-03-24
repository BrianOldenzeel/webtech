from flask import Blueprint, render_template

auth = Blueprint("auth", __name__)

@auth.route("/login")
def loginpage():
    return render_template("auth/login.html")

@auth.route("/register")
def registerpage():
    return render_template("auth/register.html")