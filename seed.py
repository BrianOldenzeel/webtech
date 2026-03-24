from app import create_app, db, bcrypt
from app.models import Instelling, User, Stage

app = create_app()

# for dummy data
with app.app_context():
    db.drop_all()
    db.create_all()

    pw = bcrypt.generate_password_hash("test").decode("utf-8")

    user1 = User(
        voornaam="Jan",
        achternaam="Jansen",
        email="jan@begeleider.com",
        password=pw,
        studie=None,
        is_student=False,
        is_begeleider=True,
        is_bedrijf_eigenaar=False,
        bedrijf=None
    )
    

    user2 = User(
        voornaam="Piet",
        achternaam="Bedrijf",
        email="piet@bedrijf.com",
        password=pw,
        studie=None,
        is_student=False,
        is_begeleider=False,
        is_bedrijf_eigenaar=True,
        bedrijf=2
    )

    user3 = User(
        voornaam="Brian",
        achternaam="Oldenzeel",
        email="blianoldenzeel@gmail.com",
        password=pw,
        studie="HBO-ICT",
        is_student=True,
        is_begeleider=False,
        is_bedrijf_eigenaar=False,
        bedrijf=None
    )

    i1 = Instelling(
        naam="Achos media",
        studie="HBO-ICT",
        locatie="Groningen",
        beschikbaar=1,
        aantal_studenten=5,
        max_aantal_studenten=5,
        totaal_uren=720
    )

    i2 = Instelling(
        naam="Heathhub Roden",
        studie="Geneeskunde",
        locatie="Roden, Groningen",
        beschikbaar=0,
        aantal_studenten=4,
        max_aantal_studenten=8,
        totaal_uren=720

    )

    i3 = Instelling(
        naam="Vitality",
        studie="Economie",
        locatie="Parijs",
        beschikbaar=1,
        aantal_studenten=3,
        max_aantal_studenten=3,
        totaal_uren=720

    )

    stage1 = Stage(
        student_id=3,
        instelling_id=1,
        status="Afgerond",
        totaal_uren=720
    )

    db.session.add_all([i1, i2, i3, stage1, user1, user2, user3])
    db.session.commit()

    print("klaar")