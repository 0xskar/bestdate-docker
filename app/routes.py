from flask import render_template, redirect, url_for, flash
from app import app
from app.forms import LoginForm


@app.route("/")
@app.route("/index")
@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    return render_template("register.html", title="Register", loggedIn=True)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash("Login requested for user {}, remember_me={}".format(form.email.data, form.remember_me.data))
        return redirect(url_for("home"))
    return render_template("login.html", title="Login", form=form)

@app.route("/logout")
def logout():
    return redirect(url_for("home"))

@app.route("/profile")
def profile():
    return render_template("profile.html", title="Profile", loggedIn=True)

@app.route("/matches")
def matches():

    return render_template("matches.html", title="Matches", loggedIn=True)

@app.route("/messages")
def messages():

    messages = [
        {
            "author": {"username": "Jane"},
            "body": "Hello how are you!?"
        },
        {
            "author": {"username": "Jill"},
            "body": "Ya i bet ya bum!!"
        }
    ]

    return render_template("messages.html", title="Messages", loggedIn=True, messages=messages)
