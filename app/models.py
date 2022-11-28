from . import db
from sqlalchemy.sql import func

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)

    def __init__(self, id, email, password):
        self.id = id
        self.email = email
        self.password = password

class Verses(db.Model):
    __bind_key__ = "NLT"
    verse = db.Column(db.String, primary_key=True)
    content = db.Column(db.String)

    def __init__(self, verse, content):
        self.verse = verse
        self.content = content

class Memorized(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey("Users.id"), primary_key=True)
    verse_id = db.Column(db.Integer, db.ForeignKey("Verses.id"))
    time_memorized = db.Column(db.DateTime(timezone=True), default=func.now())

    def __init__(self, verse_id, user_id, time_memorized):
        self.verse_id = verse_id
        self.user_id = user_id
        self.time_memorized = time_memorized