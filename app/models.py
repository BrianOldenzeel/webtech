from . import db

class Instelling(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    naam = db.Column(db.String(100))
    studie = db.Column(db.String(100))
    locatie = db.Column(db.String(100))
    beschikbaar = db.Column(db.Integer)
    aantal_studenten = db.Column(db.Integer)
    max_aantal_studenten = db.Column(db.Integer)
    totaal_uren = db.Column(db.Integer)




class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    voornaam = db.Column(db.String(100))
    achternaam = db.Column(db.String(100))
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    studie = db.Column(db.String(100))
    is_student = db.Column(db.Boolean)
    is_begeleider = db.Column(db.Boolean)
    is_bedrijf_eigenaar = db.Column(db.Boolean)
    bedrijf = db.Column(db.Integer, db.ForeignKey("instelling.id"))




class Stage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    instelling_id = db.Column(db.Integer, db.ForeignKey("instelling.id"))
    status = db.Column(db.String)
    totaal_uren = db.Column(db.Integer)
    instelling = db.relationship("Instelling", backref="stages")
    student = db.relationship("User")

