from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from .config import Config

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)


    with app.app_context():
        from . import models
        db.create_all()
        
    from .routes import init_app_routes
    init_app_routes(app)

    return app
