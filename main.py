from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mijngeheimesleutel'

class InfoForm(FlaskForm):

    instrument = StringField('Welk instrument wil je graag leren bespelen?')
    submit = SubmitField('Verzend')

@app.route("/", methods=['POST', 'GET'])
def testpage():
    return render_template('main.html')

@app.route("/login")
def loginpage():
    return render_template("/auth/login.html")

if __name__ == '__main__':
    app.run(debug=True)