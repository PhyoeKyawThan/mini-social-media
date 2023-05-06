from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    caption = db.Column(db.String(1000))
    date    = db.Column(db.String(20), nullable=False)
    imgPath = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    profile = db.Column(db.String(225))
    date    = db.Column(db.String(20), nullable=False)
    posts    = db.relationship('Post', backref='author')

