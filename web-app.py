# Test voor GIT repository
#
from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config["SECRET_KEY"] = "6a9ccbae952ca489cd80e57cc8204fff"

posts = [
    {
        "author" : "Eric Algera",
        "title" : "First Blog post",
        "content" : "Allereerster post",
        "date_posted" : "juli 2019"
    },
    {
        "author" : "Clara Bakker",
        "title" : "Tweede Blog post",
        "content" : "Een nieuwe post",
        "date_posted" : "juli 2019"
    }
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
    else:
        lash("An error has occured!", "danger")    return render_template("register.html", title="Register", form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", title="Login", form=form)

if __name__ == "__main__":
    app.run(debug=True)