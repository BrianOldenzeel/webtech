from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask_bcrypt import Bcrypt
from flask_wtf import FlaskForm

db = SQLAlchemy()
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)

    @app.context_processor
    def inject_user():
        return dict(
            user_id=session.get("user_id"),
            voornaam=session.get("user_voornaam")
        )

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SESSION_PERMANENT"] = False
    app.config["SESSION_TYPE"] = "filesystem"

    db.init_app(app)
    Session(app)
    bcrypt.init_app(app)

    # import and register routes
    from .routes.main import main
    from .routes.auth import auth
    from .routes.profiles import profiles

    app.register_blueprint(main)
    app.register_blueprint(auth)
    app.register_blueprint(profiles)

    return app