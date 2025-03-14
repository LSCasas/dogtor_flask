from ..db import db
from sqlalchemy import Integer, String, DateTime
from sqlalchemy.orm import relationship

class User(db.Model):
    """User object"""
    __tablename__ = "users"
    id = db.Column(Integer, primary_key=True)
    username = db.Column(String, unique=True, nullable=False)
    email = db.Column(String, unique=True)

class Owner(db.Model):
    """Pet owner object"""
    __tablename__ = "owners"
    id = db.Column(Integer, primary_key=True)
    first_name = db.Column(String(length=50))
    last_name = db.Column(String(length=50))
    phone = db.Column(String(length=15))
    mobile = db.Column(String(length=15))
    email = db.Column(String)

    pets = db.relationship("Pet", back_populates="owner")  # ✅ Relación corregida

pet_species_m2m = db.Table(
    "pet_species",
    db.Column("pet_id", Integer, db.ForeignKey("pets.id"), primary_key=True),
    db.Column("species_id", Integer, db.ForeignKey("species.id"), primary_key=True)
)

record_category_m2m = db.Table(
    "record_category",
    db.Column("records_id", Integer, db.ForeignKey("records.id")),
    db.Column("categories_id", Integer, db.ForeignKey("categories.id"))
)

class Species(db.Model):
    """Pet species object"""
    __tablename__ = "species"
    id = db.Column(Integer, primary_key=True)
    name = db.Column(String(length=20))

    pets = db.relationship("Pet", secondary=pet_species_m2m, back_populates="species")  # ✅ Corrección

class Pet(db.Model):
    """Pet object"""
    __tablename__ = "pets"
    id = db.Column(Integer, primary_key=True)
    name = db.Column(String(length=20))
    age = db.Column(Integer)

    owner_id = db.Column(Integer, db.ForeignKey("owners.id"))  # ✅ Agregada clave foránea
    owner = db.relationship("Owner", back_populates="pets")  # ✅ Relación corregida

    species = db.relationship("Species", secondary=pet_species_m2m, back_populates="pets")  # ✅ Corrección

    records = db.relationship("Record", back_populates="pet")  # ✅ Relación con records

class Record(db.Model):
    """Pet record object"""
    __tablename__ = "records"
    id = db.Column(Integer, primary_key=True)
    procedure = db.Column(String(length=255))
    date = db.Column(DateTime)

    pet_id = db.Column(Integer, db.ForeignKey("pets.id"))  # ✅ Clave foránea agregada
    pet = db.relationship("Pet", back_populates="records")  # ✅ Relación corregida

    categories = db.relationship("Category", secondary=record_category_m2m, back_populates="records")  # ✅ Corrección

class Category(db.Model):
    """Record category object"""
    __tablename__ = "categories"
    id = db.Column(Integer, primary_key=True)
    name = db.Column(String(length=20))

    records = db.relationship("Record", secondary=record_category_m2m, back_populates="categories")  # ✅ Corrección
