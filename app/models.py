from . import db
from sqlalchemy.sql import func

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String)
    lname = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String) 
    memorized = db.relationship("Memorized")

    def __init__(self, fname, lname, email, password, memorized):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.password = password
        self.memorized = memorized

class Memorized(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    verse_id = db.Column(db.Integer, db.ForeignKey("verses.id"))
    time_memorized = db.Column(db.DateTime(timezone=True), default=func.now())

    def __init__(self, verse_id, user_id, time_memorized):
        self.verse_id = verse_id
        self.user_id = user_id
        self.time_memorized = time_memorized

class Verses(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    version = db.Column(db.String)
    verse = db.Column(db.String)
    content = db.Column(db.String)

    def __init__(self, verse, content, version):
        self.verse = verse
        self.content = content
        self.version = version