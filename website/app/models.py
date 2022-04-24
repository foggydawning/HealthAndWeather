from tkinter import Image
from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from hashlib import md5

class User(UserMixin, db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    username: str = db.Column(db.String(64), index=True)
    email: str = db.Column(db.String(120), index=True, unique=True)
    password_hash: str = db.Column(db.String(128))
    data = db.relationship('Data', backref='user', lazy='dynamic')
    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
            digest, size)

    def __repr__(self):
        return '<User {}>'.format(self.username)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash, password)

class Data(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    user_id: int = db.Column(db.Integer, db.ForeignKey('user.id'))
    time: str = db.Column(db.String)
    well_being: int = db.Column(db.Integer)
    is_head_hurts: int = db.Column(db.Integer)
    is_high_pressure: int = db.Column(db.Integer)
    temperature: int = db.Column(db.Integer)
    magnetic_storms: int = db.Column(db.Integer)
    pressure: int = db.Column(db.Integer)
    
@login.user_loader
def load_user(id):
    return User.query.get(int(id))
