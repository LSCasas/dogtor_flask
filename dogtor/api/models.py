from ..db import db
from sqlalchemy import Integer, String
from sqlalchemy.orm import mapped_column

class User(db.Model):
    __tablename__ = 'users' 

    id = mapped_column(Integer, primary_key=True)
    username = mapped_column(String, unique=True, nullable=False)
    email = mapped_column(String, unique=True)
