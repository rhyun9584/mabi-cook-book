from app import db
from .enums import Method


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    name = db.Column(db.String(50), nullable=False)


class Cook(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    eng_name = db.Column(db.String(100), nullable=False)
    method = db.Column(db.Enum(Method), nullable=False)
    ingredients = db.Column(db.String(200), nullable=False)
