from flask import request, Blueprint, render_template, flash
from . import models, oauth, db

views = Blueprint("views", __name__)

@views.route("/", methods=["GET", "POST"])
def home():
    user = oauth.verify_access_token()
    if request.method == "POST":
        if user:
            verse = request.form.get("verse")
            if verse:
                verse_query = db.session.query(models.Verses).filter(models.Verses.contains(verse)).all()
                return render_template("results.html", results=verse_query, user=user)
            else:
                flash("Please Enter A Verse", category="error")
        else:
            flash("Please Login or Sign Up", category="error")
    return render_template("home.html", user=user)

@views.route("/search", methods=["GET", "POST"])
def results():
    user = oauth.verify_access_token()
    if request.method == "POST":
        verse = request.method.get("verse")
        return render_template("verse.html", verse=verse, user=user)
    return render_template("results.html", user=user)


@views.route("/memorized", methods=["GET", "POST"])
def get_memorized():
    user = oauth.verify_access_token()
    if request.method == "POST":
        verse = request.method.get("verse")
        return render_template("verse.html", verse=verse)
    return render_template("memorized.html", user=user)