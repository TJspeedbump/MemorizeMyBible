from flask import request, Blueprint, render_template, flash, redirect, make_response
from . import models, oauth, db

views = Blueprint("views", __name__)

@views.route("/", methods=["GET", "POST"])
def home():
    user = oauth.verify_access_token()
    if request.method == "POST":
        if user:
            verse = request.form.get("verse")
            if verse:
                verse_query = db.session.query(models.Verses).filter(models.Verses.verse.contains(verse)).all()
                return redirect("/search"), verse_query
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
    return render_template("results.html", user=user, )


@views.route("/memorized", methods=["GET", "POST"])
def get_memorized():
    user = oauth.verify_access_token()
    if request.method == "POST":
        verse = request.method.get("verse")
        redirect("/search", verse=verse)
        return 
    return render_template("memorized.html", user=user)