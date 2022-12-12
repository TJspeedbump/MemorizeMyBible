from flask import request, Blueprint, render_template, flash, redirect, make_response, Response, session
from . import models, oauth, db

views = Blueprint("views", __name__)

@views.route("/", methods=["GET", "POST"])
def home():
    user = oauth.verify_access_token()
    if request.method == "POST":
        if user:
            verse = request.form.get("verse")
            if verse:
                session["verse"] = verse
                return redirect("/search")
            else:
                flash("Please Enter A Verse", category="error")
        else:
            flash("Please Login or Sign Up", category="error")
    return render_template("home.html", user=user)

@views.route("/search", methods=["GET", "POST"])
def search():
    user = oauth.verify_access_token()
    verse = session.get("verse")
    verse_query = db.session.query(models.NLT_Verses).filter(models.NLT_Verses.verse.contains(verse)).all()
    if not verse_query:
        flash("Sorry, We Could Not Find Any Verses With That Naming", category="error")
    if request.method == "POST":
        verse = request.method.get("verse")
        return render_template("verse.html", verse=verse, user=user)
    return render_template("results.html", user=user, verse_query=verse_query)

@views.route("/verse-breakdown", methods=["GET", "POST"])
def verse_breakdown():
    user = oauth.verify_access_token()
    verse = session.get("verse")
    return render_template("verse_breakdown.html", user=user, verse=verse)


@views.route("/memorized", methods=["GET", "POST"])
def get_memorized():
    user = oauth.verify_access_token()
    if request.method == "POST":
        verse = request.method.get("verse")
        redirect("/search", verse=verse)
        return 
    return render_template("memorized.html", user=user)