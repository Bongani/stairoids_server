from flask import request, jsonify

from app import app, db
from app.models import Event
import logging

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route("/event", methods=["POST"])
def add_event():
    logging.info(":::START::: add_event")
    username = request.get_json().get('username')
    location = request.get_json().get('location')
    time = request.get_json().get('time')

    new_event = Event(username, location, time)

    db.session.add(new_event)
    db.session.commit()

    logging.info(":::END::: add_event")
    return jsonify(success=True)