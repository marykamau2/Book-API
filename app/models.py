from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from datetime import datetime


class Books:
    
    def __init__(self, id,title,subtitle,authors, description, thumbnail, saleability):
        self.id = id
        self.title=title
        self.subtitle = subtitle
        self.authors = authors
        self.description = description
        self.thumbnail = thumbnail
        self.saleability = saleability

class User(UserMixin, db.Model):
    __tablename__ = 'users_table'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    pass_secure  = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)

    def __repr__(self):
        return f'User {self.username}'


    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)