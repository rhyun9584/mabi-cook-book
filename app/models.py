from sqlalchemy.dialects.mysql import TINYINT

from app import db
from .enums import Method


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)


class Cook(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    eng_name = db.Column(db.String(100), nullable=False)
    method = db.Column(db.Enum(Method), nullable=False)
    ingredients = db.Column(db.String(200), nullable=False)


class Collect(db.Model):
    user = db.Column(db.ForeignKey('user.id'), nullable=False, primary_key=True)
    cook = db.Column(db.ForeignKey('cook.id'), nullable=False, primary_key=True)
    # 수집 상태 || 0: 미수집, 1: 수집, 2: 5성 수집
    state = db.Column(TINYINT, nullable=False, default=0)
