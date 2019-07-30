from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SECRET_KEY"] = "6a9ccbae952ca489cd80e57cc8204fff"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"  # Relative path
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

from flaskblog import routes
