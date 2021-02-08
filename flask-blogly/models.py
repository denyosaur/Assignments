"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
default_img = 'https://blog.nscsports.org/wp-content/uploads/2014/10/default-img.gif'

    
class Users(db.Model):
    __tablename__='users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    first_name = db.Column(db.Text, nullable=False)

    last_name = db.Column(db.Text, nullable=False)

    img_url = db.Column(db.Text, nullable=False, default=default_img)


def connect_db(app):
    db.app = app
    db.init_app(app)