#installization
#pip install sqlalchemy
#pip install Flask-SQLAlchemy

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
#dialect+driver://username:password@host:port/database

app.config['SQLALCHEMY_DATABASE_URI'] = 'king_app_devb:!ac-okl.34.731@127.0.0.1/king'

db = SQLAlchemy(app)


class Catgory(db.Model):
    category_id = db.Column(db.Integer, primary_key=True)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username