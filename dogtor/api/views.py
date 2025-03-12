from flask import request

from . import api_blueprint


users_data = [
        {"id": 1, "username": "alfredo", "email": "luis@hotmail.com"},
        {"id": 2, "username": "user1", "email": "123"},
        {"id": 3, "username": "user1", "email": "123"}
    ]

@api.route("/users/<int:user_id>", methods=["GET", "PUT", "DELETE"])
@api.route("/users/", methods=["GET", "POST"])
def users(user_id=None):
    if user_id is not None:
        found_user = None
        for user in users_data:
            if user["id"] == user_id:
                found_user = user

        if request.method == "PUT":
            return {"detail": f"user {found_user['username']} modified"}
        if request.method == "DELETE":
            return {"detail": f"user {found_user['username']} deleted"}

        return found_user

    if request.method == "POST":
        data = request.data
        return {"detail": f"user {data['username']} created"}
    return users_data


@api.route("/pets/")
def pets():
    return []

@api.route("/owners/")
def owners():
    return []

@api.route("/procedures/")
def owners():
    return []

@api.route("/species/")
def owners():
    return []


            