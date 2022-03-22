from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flask_image_alchemy.fields import StdImageField
from flask_image_alchemy.storages import S3Storage

storage = S3Storage()
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    data = db.relationship('Data', backref='user', lazy='dynamic')
    image = db.Column(
        StdImageField(
            storage=storage,
            variations={
                'thumbnail': {"width": 100, "height": 100, "crop": True}
            }
        ), nullable=True
    )

    def __repr__(self):
        return '<User {}>'.format(self.username)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash, password)

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    time = db.Column(db.String)
    well_being = db.Column(db.Integer)
    is_head_hurts = db.Column(db.Integer)
    is_high_pressure = db.Column(db.Integer)
    temperature = db.Column(db.Integer)
    pressure = db.Column(db.Integer)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
