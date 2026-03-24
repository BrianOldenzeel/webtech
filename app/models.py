from . import db

class Instelling(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    naam = db.Column(db.String(100))
    soort = db.Column(db.String(100))


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    voornaam = db.Column(db.String(100))
    achternaam = db.Column(db.String(100))


class Stage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    begeleider_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    instelling_id = db.Column(db.Integer, db.ForeignKey("instelling.id"))
    cijfer = db.Column(db.Integer)
    periode = db.Column(db.String(100))