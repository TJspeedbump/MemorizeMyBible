from . import db
from sqlalchemy.sql import func

class Memorized(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), primary_key=True)
    verse_id = db.Column(db.Integer, db.ForeignKey("verses.id"))
    time_memorized = db.Column(db.DateTime(timezone=True), default=func.now())

    def __init__(self, verse_id, user_id, time_memorized):
        self.verse_id = verse_id
        self.user_id = user_id
        self.time_memorized = time_memorized

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String)
    lname = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)

    def __init__(self, id, email, password):
        self.id = id
        self.email = email
        self.password = password

class Verses(db.Model):
    __bind_key__ = "NLT"
    id = db.Column(db.Integer, primary_key=True)
    verse = db.Column(db.String)
    content = db.Column(db.String)

    def __init__(self, verse, content):
        self.verse = verse
        self.content = content

class Verses(db.Model):
    __bind_key__ = "NIV"
    id = db.Column(db.Integer, primary_key=True)
    verse = db.Column(db.String)
    content = db.Column(db.String)

    def __init__(self, verse, content):
        self.verse = verse
        self.content = content