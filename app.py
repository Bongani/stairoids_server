from flask import request, jsonify
from app.models import Event
from app import db, app


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


@app.route("/event", methods=["POST"])
def add_event():
    app.logger.info(":::START::: add_event")
    username = request.get_json().get('username')
    location = request.get_json().get('location')
    time = request.get_json().get('time')

    app.logger.debug("adding to DB: {} {} {}".format(username, location, time))

    new_event = Event(username, location, time)

    db.session.add(new_event)
    db.session.commit()

    app.logger.info(":::END::: add_event")
    return jsonify(success=True)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, host='0.0.0.0', port=9000)

