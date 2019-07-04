''' Models '''

from FlaskRTBCTF import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    #rank = db.Column(db.Integer, unique=True, nullable=False)
    # score = db.Column(db.Integer, default=0)

class Score(db.Model):
    userid=db.Column(db.Integer, primary_key=True)
    userHash = db.Column(db.Boolean)
    rootHash = db.Column(db.Boolean)
    score = db.Column(db.Integer)

    


