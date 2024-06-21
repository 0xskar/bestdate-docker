from flask import render_template, redirect, url_for, flash, request
from urllib.parse import urlsplit
from app import app, db
from app.forms import LoginForm, RegistrationForm
from app.models import User
from flask_login import current_user, login_user, logout_user, login_required
import sqlalchemy as sa


@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    form = RegistrationForm()
    if form.validate_on_submit():
        # Create user model and add to database
        user = User(username=form.username.data,
                    email=form.email.data,
                    first_name=form.first_name.data,
                    last_name=form.last_name.data,
                    date_of_birth=form.date_of_birth.data,
                    gender=form.gender.data,
                    location=form.location.data
                    )
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("You're now registered, login and setup your profile so you can begin getting matches!")
        return redirect(url_for('login'))
    return render_template("register.html", title="Register", form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.scalar(sa.select(User).where(User.email == form.email.data))
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password.')
            return redirect(url_for('login'))
        
        login_user(user, remember=form.remember_me.data)

        # if the user is trying to login to a non-authorized route this will send them back to the page once authorized. 
        # if the URL inclused a full URL that inclused a domain name then the URL (netloc) is ignored (for security) and redirected to the index page 
        next_page = request.args.get('next')
        if not next_page or urlsplit(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    
    return render_template("login.html", title="Login", form=form)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/profile")
@login_required
def profile():
    return render_template("profile.html", title="Profile")

@app.route("/matches")
@login_required
def matches():

    return render_template("matches.html", title="Matches")

@app.route("/messages")
@login_required
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

    return render_template("messages.html", title="Messages", messages=messages)
