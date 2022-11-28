from flask import request, Blueprint, render_template
from . import models, oauth, db

views = Blueprint("views", __name__)

@views.route("/", methods=["GET"])
def home():
    user = oauth.verify_access_token()
    return render_template("home.html", user=user)

@views.route("/search", methods=["GET", "POST"])
def search_verse():
    user = oauth.verify_access_token()
    if request.method == "POST":
        verse = request.form.get("verse")
        verse_query = db.session.query(models.Verses).filter(models.Verses.contains(verse)).all()
    return render_template("results.html", results=verse_query, user=user)


@views.route("/memorized", methods=["GET", "POST"])
def get_memorized():
    user = oauth.verify_access_token()
    return render_template("memorized.html", user=user)