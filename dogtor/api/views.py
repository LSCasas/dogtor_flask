from datetime import datetime, timedelta, timezone
import jwt
from functools import wraps
from flask import request, make_response, jsonify
from dogtor.api import api_blueprint
from werkzeug.security import generate_password_hash, check_password_hash  
from . import models
from ..db import db

users_data = [
    {"id": 1, "username": "alfredo", "email": "luis@hotmail.com"},
    {"id": 2, "username": "user1", "email": "123"},
    {"id": 3, "username": "user1", "email": "123"}
]

def token_required(func):
    @wraps(func)
    def wrapper():
        """Validation of token"""
        from dogtor import Config
        authorization = request.headers.get("Authorization")
        prefix = "Bearer "
        if not authorization:
            return {"detail": "Missing 'Authorization' header"}, 401
        
        if not authorization.startswith(prefix):
            return {"detail": "Invalid token prefix"}, 401
        
        token = authorization.split(" ")[1]
        if not token:
            return {"detail": "Missing token"}, 401
        try:
            payload = jwt.decode(token, Config.SECRET_KEY, algorithms=["HS256"])
        
        except jwt.exceptions.ExpiredSignatureError:
            return {"detail": "Token expired"}, 401
        except jwt.exceptions.InvalidAlgorithmError:
            return {"detail": "Invalid token"}
        
        request.user = db.session.execute(
        db.select(models.User).where(models.User.id == payload["sub"])
        ).scalar_one()

        return func()
    return wrapper
    
@api_blueprint.route("/profile/", methods=["POST"])
@token_required
def mi_funcion():
    user = request.user
    return {
        "first_name": user.first_name,
        "last_name": user.last_name,
        "email": user.email
    }


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

@api_blueprint.route("/owners/", methods=["POST"])
@token_required
def owners():
    return []

@api_blueprint.route("/procedures/")
def procedures():  
    return []


@api_blueprint.route("/species/<int:species_id>", methods=["GET", "PUT", "DELETE"])
@api_blueprint.route("/species/", methods=["GET", "POST"])
def species(species_id=None):
    if species_id is not None:
        species = models.Species.query.get_or_404(species_id)

        if request.method == "GET":
            return {"id": species.id, "name": species.name}

        elif request.method == "PUT":
            data = request.get_json()
            species.name = data['name']
            db.session.commit()
            return {"detail": f"Species {species.name} updated successfully"}

        elif request.method == "DELETE":
            species_name = species.name
            db.session.delete(species)
            db.session.commit()
            return {"detail": f"Species {species_name} deleted successfully"}

    else:
        if request.method == "GET":
            species_all = models.Species.query.all()
            return [{"id": species.id, "name": species.name} for species in species_all]

        elif request.method == "POST":
            data = request.get_json()
            species_instance = models.Species(name=data['name'])
            db.session.add(species_instance)
            db.session.commit()
            return {"detail": f"Species {species_instance.name} created successfully"}


@api_blueprint.route("/signup/", methods=["POST"])
def signup():
    data = request.get_json()
    email = data.get("email")

    if not email:
        return {"detail": "email is required"}, 400
    
    user_exists = db.session.execute(
        db.select(models.User).where(models.User.email == email) 
    ).scalar_one_or_none()

    if user_exists:
        return {"detail": "email already taken"}, 400
    
    password = data.get("password")
    user = models.User(
        first_name = data.get("first_name"),
        last_name = data.get("last_name"),
        email = email,
        password=generate_password_hash(password)
    )
    db.session.add(user)
    db.session.commit()
    return {"detail": "user created successufully"}, 201


@api_blueprint.route("/login/", methods=["POST"])
def login():
    """Login on app user """
    from dogtor import Config
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return {"detail": "email or password missiing"}, 400
    
    user = db.session.execute(
        db.select(models.User).where(models.User.email ==  email)
    ).scalar_one_or_none()

    
    if not check_password_hash(user.password, password):
        return {"detail": "invalid password or password"}, 401
    
    token = jwt.encode({"sub": str(user.id),
                        "iat": datetime.now(),
                "exp": datetime.now(timezone.utc) + timedelta(minutes=30),
                },
                Config.SECRET_KEY,
                algorithm="HS256"
                )

    return jsonify({"token": token})
    
