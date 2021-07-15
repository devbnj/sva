# models.py

from flask_login import UserMixin
from . import db

# def class
class User(UserMixin, db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key = True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique = True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    bgcode = db.Column(db.String(100))
# end def

# def class
class Vivek(db.Model):
    __tablename__ = "vivek"
    id = db.Column(db.Integer, primary_key = True)
    sayings = db.Column(db.Text)
    
    def __repr__(self):
        return "<Vivek(sayings='%s')>" % (self.sayings)
# end def

    