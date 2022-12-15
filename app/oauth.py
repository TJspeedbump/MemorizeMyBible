from flask import request, redirect
from passlib.hash import sha256_crypt
import jwt
from datetime import timedelta, datetime
from dotenv import load_dotenv
import os
from . import models, db

load_dotenv()

def create_access_token(user):
    token = jwt.encode({"user": user, "exp": datetime.utcnow() + timedelta(minutes=int(os.getenv("Token_Access_Minutes")))}, os.getenv("SECRET_KEY"), algorithm=os.getenv("ALGORITHM"))
    return token

def verify_access_token():
    try:
        token = request.cookies.get("token")
        payload = jwt.decode(token, os.getenv("SECRET_KEY"), algorithms=os.getenv("ALGORITHM"))
        user = payload.get("user")
        user = db.session.query(models.Users).filter(models.Users.id==user).first()
        if user:
            return user
        return None
    except:
        return None

def hash_password(password):
    hash = sha256_crypt.hash(password)
    return hash

def verify_hash_password(password, user_password):
    check = sha256_crypt.verify(password, user_password)
    return check

def create_cookie(name, value, age):
    cookie = redirect("/")
    cookie.set_cookie(name, value=value, expires=age, httponly=True)
    return cookie

def convert_sql(string):
    strverse = ""
    for i in range(len(string)):
        if not i == 0 and not i == (len(string)-2) and not i == (len(string)-1):
            strverse += string[i]
    return strverse