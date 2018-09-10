from app import db


class UserBoard(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    fastest_time = db.Column(db.Integer, index=True, unique=True)

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Event(db.Model):
    event_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True)
    location = db.Column(db.Integer)
    time = db.Column(db.Integer, index=True)

    def __init__(self, username, location, time):
        self.username = username
        self.location = location
        self.time = time
