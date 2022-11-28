from flask import Flask
from dotenv import load_dotenv
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
db = SQLAlchemy(app)

def create_app():
    load_dotenv()
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("USER_DATABASE_URL")
    app.config['SQLALCHEMY_BINDS'] = {"NLT": os.getenv("NLT_DATABASE_URL"), 
                                      "NIV": os.getenv("NIV_DATABASE_URL")}
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

    migrate = Migrate(app, db)
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    db.create_all(app)
    
    return app

db = SQLAlchemy(app)