from flask import Flask
from dotenv import load_dotenv
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    load_dotenv()
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("USER_DATABASE_URL")
    app.config['SQLALCHEMY_BINDS'] = {"NLT": os.getenv("NLT_DATABASE_URL"), 
                                      "NIV": os.getenv("NIV_DATABASE_URL")}
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
    db.init_app(app)

    from .models import Users, Verses, Memorized

    migrate = Migrate(app, db)
    # create_databases(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")
    
    return app

# def create_databases(app):
#     db.create_all(app)
#     print("Created Database!!!")