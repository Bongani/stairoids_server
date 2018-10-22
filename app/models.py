from app import db


class Event(db.Model):
    event_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True)
    location = db.Column(db.Integer)
    time = db.Column(db.Integer, index=True)

    def __init__(self, username, location, time):
        self.username = username
        self.location = location
        self.time = time
