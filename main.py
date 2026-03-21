from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session

app = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.config["SESSION_PERMANENT"] = False     # Sessions expire when the browser is closed
app.config["SESSION_TYPE"] = "filesystem"     # Store session data in files

db = SQLAlchemy(app)
Session(app)

class student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    voornaam = db.Column(db.String(100))
    achternaam = db.Column(db.String(100))

class instelling(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    naam = db.Column(db.String(100))
    soort = db.Column(db.String(100))

class begeleider(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    voornaam = db.Column(db.String(100))
    achternaam = db.Column(db.String(100))

class stage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey("student.id"))
    begeleider_id = db.Column(db.Integer, db.ForeignKey("begeleider.id"))
    instelling_id = db.Column(db.Integer, db.ForeignKey("instelling.id"))
    cijfer = db.Column(db.Integer)
    periode = db.Column(db.String(100))

@app.route("/", methods=['POST', 'GET'])
def testpage():
    return render_template('main.html')

@app.route("/login")
def loginpage():
    return render_template("/auth/login.html")

@app.route("/register")
def registerpage():
    return render_template("/auth/register.html")

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)