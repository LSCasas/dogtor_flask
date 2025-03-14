from flask import request
from dogtor.api import api_blueprint  
from . import models
from ..db import db

users_data = [
    {"id": 1, "username": "alfredo", "email": "luis@hotmail.com"},
    {"id": 2, "username": "user1", "email": "123"},
    {"id": 3, "username": "user1", "email": "123"}
]

@api_blueprint.route("/users/<int:user_id>", methods=["GET", "PUT", "DELETE"])
@api_blueprint.route("/users/", methods=["GET", "POST"])
def users(user_id=None):
    if user_id is not None:
        found_user = next((user for user in users_data if user["id"] == user_id), None)
        if not found_user:
            return {"error": "User not found"}, 404
        
        if request.method == "PUT":
            return {"detail": f"user {found_user['username']} modified"}
        if request.method == "DELETE":
            return {"detail": f"user {found_user['username']} deleted"}

        return found_user

    if request.method == "POST":
        data = request.get_json()  
        return {"detail": f"user {data['username']} created"}

    return users_data

@api_blueprint.route("/pets/")
def pets():
    return []

@api_blueprint.route("/owners/")
def owners():
    return []

@api_blueprint.route("/procedures/")
def procedures():  
    return []

@api_blueprint.route("/species/", methods=["POST"])
def species():
    data = request.get_json()
    species_instance = models.Species(name=data['name'])
    db.session.add(species_instance)
    db.session.commit()
    return {"detail": f"species{species_instance.name} created successfully"}
