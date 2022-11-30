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
        print("Cool")
        token = request.cookies.get("token")
        print("True")
        payload = jwt.decode(token, os.getenv("SECRET_KEY"), algorithms=os.getenv("ALGORITHM"))
        print("Problem")
        user = payload.get("user")
        # user = db.session.query(models.Users).filter(models.Users==user).first()
        if user:
            return user
        return None
    except:
        print("Bad")
        return None

def hash_password(password):
    hash = sha256_crypt.hash(password)
    return hash

def verify_hash_password(password, user_password):
    check = sha256_crypt.verify(password, user_password)
    return check
