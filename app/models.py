from sqlalchemy import Column
from app import db
from werkzeug.security import generate_password_hash, check_password_hash


class City(db.Model):
    __tablename__ = 'city'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = Column(db.String)
    img = Column(db.String)



class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

#class City(db.Model):
#    id = Column(db.Integer)
#    img = Column(db.String)
#    description = Column(db.String)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def is_password_correct(self, password) -> bool:
        return check_password_hash(self.password_hash, password)

    def to_json(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
        }

    def __str__(self):
        return str(self.id) + ': ' + self.email



