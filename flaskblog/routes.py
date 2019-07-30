from flask import render_template, url_for, flash, redirect
from flaskblog import app
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post


posts = [
    {
        "author": "Eric Algera",
        "title": "First Blog post",
        "content": "Allereerster post",
        "date_posted": "juli 2019",
    },
    {
        "author": "Clara Bakker",
        "title": "Tweede Blog post",
        "content": "Een nieuwe post",
        "date_posted": "juli 2019",
    },
]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for: {form.username.data}!", "success")
        return redirect(url_for("home"))
    # else:
    #    flash(f"An error has occured!", "danger")
    return render_template("register.html", title="Register", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@blog.com" and form.password.data == "password":
            flash("You have been logged in!", category="success")
            return redirect(url_for("home"))
        else:
            flash("Login unsuccesful. Check username / password", category="danger")
    return render_template("login.html", title="Login", form=form)
