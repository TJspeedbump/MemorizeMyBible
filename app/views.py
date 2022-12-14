from flask import request, Blueprint, render_template, flash, redirect, make_response, Response, session
from . import models, oauth, db
from sqlalchemy import *

views = Blueprint("views", __name__)


@views.route("/", methods=["GET", "POST"])
def home():
    user = oauth.verify_access_token()
    if request.method == "POST":
        if user:
            search = request.form.get("search")
            if search:
                session["search"] = search
                return redirect("/search")
            else:
                flash("Please Enter A Verse", category="error")
        else:
            flash("Please Login or Sign Up", category="error")
    return render_template("home.html", user=user)


@views.route("/search", methods=["GET", "POST"])
def search():
    user = oauth.verify_access_token()
    if not user:
        return render_template("no_user.html")
    search = session.get("search")
    verse_query = db.session.query(models.Verses).filter(models.Verses.verse.contains(search)).all()
    if not verse_query:
        flash("Sorry, We Could Not Find Any Verses With That Naming", category="error")
    if request.method == "POST":
        verse = request.form.get("verse")
        session["verse"] = verse
        return render_template("verse_breakdown.html", verse=verse, user=user)
    return render_template("results.html", user=user, verse_query=verse_query)


@views.route("/verse-breakdown", methods=["GET", "POST"])
def verse_breakdown():
    user = oauth.verify_access_token()
    if not user:
        return render_template("no_user.html")
    verse = session.get("verse")
    return render_template("verse_breakdown.html", user=user, verse=verse)


@views.route("/memorized", methods=["GET", "POST"])
def get_memorized():
    user = oauth.verify_access_token()
    if not user:
        return render_template("no_user.html")
    list = []
    verses = db.session.query(models.Memorized.verse_id).filter(models.Memorized.user_id==user.id).all()
    for verse in verses:
        num = str(verse)
        for i in num:
            if i.isdigit():
                num = i
                break
        list += db.session.query(models.Verses.verse).filter(models.Verses.id==num).first()
    if request.method == "POST":
        verse = request.form.get("verse")
        session["verse"] = verse
        return redirect("/verse-breakdown")
    return render_template("memorized.html", user=user, verses=list)