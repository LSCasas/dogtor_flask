from flask import Flask
from .api import api_blueprint 
from .config import Config
from .db import db

def create_app():
    app = Flask(__name__)
    
    app.config.from_object(Config)
    print(app.config)

    db.init_app(app)

    app.register_blueprint(api_blueprint)  

    return app
