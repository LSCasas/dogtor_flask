from flask import Flask
from .api import api_blueprint
from .config import Config
from .db import db

def create_app():
    app = Flask(__name__)
    
    app.config.from_object(Config)
    db.init_app(app)

    app.register_blueprint(api_blueprint)

    @app.route("/init_db")
    def init_db():
        with app.app_context():
            db.create_all()
        return "Database created"
    
    @app.route("/drop_db")
    def drop_db():
        with app.app_context():
            db.drop_all()
        return "Database dropped"

    return app
