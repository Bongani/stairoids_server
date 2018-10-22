from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask import request, jsonify
import logging

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
db.create_all()


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


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


@app.route("/event", methods=["POST"])
def add_event():
    print(request)
    logging.info(":::START::: add_event")
    username = request.get_json().get('username')
    location = request.get_json().get('location')
    time = request.get_json().get('time')

    print("{} {} {}".format(username, location, time))

    # new_event = Event(username, location, time)
    #
    # db.session.add(new_event)
    # db.session.commit()
    #
    # logging.info(":::END::: add_event")
    return jsonify(success=True)





if __name__ ==  '__main__':
    app.run(debug=True, host='0.0.0.0')

