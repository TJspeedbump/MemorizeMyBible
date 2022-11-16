from flask import request
from passlib.hash import sha256_crypt
import jwt
import datetime
from dotenv import load_dotenv
import os
from . import models, db

load_dotenv()

def create_access_token(user):
    token = jwt.encode({"user": user, "exp": datetime.datetime.utcnow()+datetime.timedelta(int(os.getenv("Token_Access_Minutes")))}, os.getenv("SECRET_KEY"), algorithm=os.getenv("ALGORITHM"))
    return token

def verify_access_token():
    try:
        token = request.cookie.get("token")
        payload = jwt.decode(token, os.getenv("SECRET_KEY"), algorithm=os.getenv("ALGORITHM"))
        user_id = payload.get("user")
        user = db.session.query(models.Users).filter(models.User.id==user_id).first()
        if user:
            return user
        return None
    except:
        return None

def hash_password(password):
    sha256_crypt.hash(password)

def verify_hash_password(password, user_password):
    sha256_crypt.verify(password, user_password)