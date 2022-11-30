from flask import request, Blueprint, flash, render_template, make_response
from . import oauth, models, db

auth = Blueprint("auth", __name__)

@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        if email:
            user = db.session.query(models.Users).filter(models.Users.email==email).first()
            if user:
                if oauth.verify_hash_password(password, user.password):
                    token = oauth.create_access_token(user)
                    res = make_response(render_template("home.html"))
                    res.set_cookie("token", value=token, expires=None, httponly=True)
                    return res
                else:
                    flash("Please enter a valid email and password", category="error")
            else:
                flash("Please enter a valid email and password", category="error")
        else:
            flash("Please enter your email and password", category="error")
    return render_template("login.html")

@auth.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        fname = request.form.get("Fname")
        lname = request.form.get("Lname")
        email = request.form.get("email")
        password = request.form.get("password")
        repassword = request.form.get("repassword")
        if password != repassword:
            flash("Your Passwords Did not Match, Please Re-Enter", category="error")
        else:
            if fname and lname and email and password:
                user = db.session.query(models.Users).filter(models.Users.email==email).first()
                if not user:
                    new_user = models.User(fname=fname, lname=lname, email=email, password=password)
                    db.session.add(new_user)
                    db.session.commit()
                    return render_template("home.html")
                else:
                    flash("Please enter a valid email and password", category="error")
            else:
                flash("Please enter your Infromation", category="error")
    return render_template("signup.html")


@auth.route("/logout", methods=["POST"])
def logout():
    return render_template("login.html")