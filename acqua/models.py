from werkzeug.security import generate_password_hash, check_password_hash
from . import db, lm
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(16), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    acqdim = db.relationship('Acqdim', uselist=False, backref='users')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    @staticmethod
    def register(username, password, email):
        user = User(username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()

    def __repr__(self):
        return '<User {0}>'.format(self.username)

class Acqdim(db.Model):
    __tablename__= 'acquadimension'
    id = db.Column(db.Integer, primary_key=True)
    height = db.Column(db.Integer)
    lenght = db.Column(db.Integer)
    width = db.Column(db.Integer)
    users_id = db.Column(db.Integer, db.ForeignKey('users.id'))

def addim(height, lenght, width, users):
    info = Acqdim(height=height, lenght=lenght, width=width, users=users)
    db.session.add(info)
    db.session.commit()

def deldim():
    data = Acqdim.query.order_by(Acqdim.height.desc()).all()
    for x in data:
        if x.users == None:
            db.session.delete(x)
            db.session.commit()


@lm.user_loader
def load_user(id):
    return User.query.get(int(id))
