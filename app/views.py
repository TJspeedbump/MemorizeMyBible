from flask import request, Blueprint, render_template, flash, redirect, make_response, Response
from . import models, oauth, db

views = Blueprint("views", __name__)

@views.route("/", methods=["GET", "POST"])
def home():
    user = oauth.verify_access_token()
    if request.method == "POST":
        if user:
            verse = request.form.get("verse")
            if verse:
                res = make_response(redirect("/search"))
                res.headers["verse"] = verse
                return res
            else:
                flash("Please Enter A Verse", category="error")
        else:
            flash("Please Login or Sign Up", category="error")
    return render_template("home.html", user=user)

@views.route("/search", methods=["GET", "POST"])
def results():
    user = oauth.verify_access_token()
    verse = request.headers.get("verse")
    print(str(verse) + "cool")
    # verse_query = db.session.query(models.NLT_Verses).filter(models.NLT_Verses.verse.contains(verse)).all()
    if request.method == "POST":
        verse = request.method.get("verse")
        return render_template("verse.html", verse=verse, user=user)
    print("cook")
    return render_template("results.html", user=user, verse_query=verse_query)


@views.route("/memorized", methods=["GET", "POST"])
def get_memorized():
    user = oauth.verify_access_token()
    if request.method == "POST":
        verse = request.method.get("verse")
        redirect("/search", verse=verse)
        return 
    return render_template("memorized.html", user=user)