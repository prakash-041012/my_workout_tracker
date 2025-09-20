from . import db
from flask_login import UserMixin
from datetime import datetime

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(100))
    gender = db.Column(db.String(100))
    password = db.Column(db.String(100))
    workouts = db.relationship('Workout', backref='author', lazy=True)

class Workout(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    count = db.Column(db.Integer, nullable=False)
    works = db.Column(db.String(200), nullable=False)
    dateposted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    description = db.Column(db.Text,nullable=False)
    users_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
