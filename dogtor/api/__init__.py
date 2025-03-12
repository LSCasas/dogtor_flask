from flask import Blueprint
from . import views

api_blueprint = Blueprint("api", __name__, url_prefix="/api")