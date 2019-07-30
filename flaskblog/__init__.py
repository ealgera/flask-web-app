from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
app.config["SECRET_KEY"] = "6a9ccbae952ca489cd80e57cc8204fff"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"  # Relative path
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"  # Function in 'routes'
login_manager.login_message_category = "info"

from flaskblog import routes
