from flask_sqlalchemy import SQLAlchemy

import bcrypt

import os

db = SQLAlchemy()


class User(db.Model):
    """Data model for a user."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password_hashed = db.Column(db.LargeBinary(128), nullable=False)

    def get_hash(password):
        return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt(15))

    def check_password(self, password):
        encoded_password = password.encode("utf-8")
        return bcrypt.checkpw(encoded_password, self.password_hashed)

    def __repr__(self):
        """Display info about User."""

        return f'<User user_id={self.user_id}, username={self.username}, email={self.email}>'


class Image(db.Model):
    """Data model for an image."""

    __tablename__ = "images"

    image_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    url = db.Column(db.String, nullable=False)
    notes = db.Column(db.String)
    private = db.Column(db.Boolean, nullable=False)
    time = db.Column(db.DateTime, nullable=False)
    # FK user
    # FK tag


    def __repr__(self):
        """Display info about Image."""

        return f'<User image_id={self.image_id}, url={self.url}, date={self.date}>'


def connect_to_db(flask_app, db_uri='postgresql:///pt', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    # flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')    


if __name__ == '__main__':
    print("we're in model")
    from server import app

    connect_to_db(app)