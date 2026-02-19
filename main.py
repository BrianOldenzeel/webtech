from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mijngeheimesleutel'

class InfoForm(FlaskForm):

    instrument = StringField('Welk instrument wil je graag leren bespelen?')
    submit = SubmitField('Verzend')

@app.route("/", methods=['POST', 'GET'])
def testpage():
    instrument = False
    # Maak een object van de klasse InfoForm aan.
    form = InfoForm()
    # Als het formulier valide is
    if form.validate_on_submit():
        # Haal de data voor instrument op uit het formulier.
        instrument = form.instrument.data
        # Zet de waarde voor de variabele instrument op het formulier weer op False
        form.instrument.data = ''
        return render_template('main.html', form=form, instrument=instrument)
    return render_template('main.html', form=form)

@app.route("/login")
def loginpage():
    return render_template("/auth/login.html")

if __name__ == '__main__':
    app.run(debug=True)