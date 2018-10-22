from flask import Flask
from werkzeug.routing import IntegerConverter

from config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)


# Adds support for signed integers in the flask route (for negative floor numbers when descending)
class SignedIntConverter(IntegerConverter):
    regex = r'-?\d+'


app.url_map.converters['signed_int'] = SignedIntConverter

db = SQLAlchemy(app)
db.create_all()
