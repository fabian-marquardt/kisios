from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)


def activate_testing_mode():
    app.config['TESTING'] = True
    app.config['DEBUG'] = True


