from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    click_count = db.Column(db.Integer)

    def __init__(self, username):
        self.username = username
        self.click_count = 0

    def __repr__(self):
        return self.username