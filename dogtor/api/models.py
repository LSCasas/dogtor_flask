from ..db import db
from sqlalchemy import Integer, String, DateTime
from sqlalchemy.orm import mapped_column, relationship

class User(db.Model):
    """User object"""
    __tablename__ = "users"
    id = db.Column(Integer, primary_key=True)
    username = db.Column(String, unique=True, nullable=False)
    email = db.Column(String, unique=True)

class Owner(db.Model):
    """Pet owner object """
    __tablename__ = "owners"
    id = db.Column(Integer, primary_key=True)
    first_name = db.Column(String(length=50))
    last_name = db.Column(String(length=50))
    phone = db.Column(String(length=15))
    mobile = db.Column(String(length=15))
    email = db.Column(String)
    # pet_id = db.Column(Integer, db.ForeignKey("pets.id"))


pet_species_m2m = db.Table(
    "pet_species",
    db.Column("pet_id", Integer, db.ForeignKey("pets.id")),  # Corregido
    db.Column("species_id", Integer, db.ForeignKey("species.id"))
)

class Species(db.Model):
    "Pet species object "
    __tablename__ = "species"
    id = db.Column(Integer, primary_key=True)
    name = db.Column(String(length=20))
    pets = db.relationship("Pet", secondary=pet_species_m2m, backref="species")

class Pet(db.Model):
    """Pet object"""
    __tablename__ = "pets"
    id = db.Column(Integer, primary_key=True)
    name = db.Column(String(length=20))
    owner = db.relationship("Owner", backref="pets")
    age = db.Column(Integer)
    species = db.relationship("Species", secondary=pet_species_m2m, backref="pets")
    #species_id = db.relationship("Species", secondary=pet_species_m2m, backref="pets")

class Record(db.Model):
    """Pet record object"""
    __tablename__ = "records"
    id = db.Column(Integer, primary_key=True)
    category = db.Column(String(length=20))
    procedure = db.Column(String(length=255))
    pet_id = db.Column(Integer, db.ForeignKey("pets.id"))
    pet = db.relationship("Pet", backref="records")
    date= db.Column(DateTime)