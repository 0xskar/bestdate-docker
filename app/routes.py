import os
import base64
from flask import render_template, redirect, url_for, flash, request
from werkzeug.utils import secure_filename
from flask_login import current_user, login_user, logout_user, login_required
from urllib.parse import urlsplit
from app import app, db
from app.forms import LoginForm, RegistrationForm, ProfileForm
from app.models import User
import sqlalchemy as sa
from sqlalchemy.orm.attributes import flag_modified


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
        # Check if username or email already exists in the database
        existing_user = User.query.filter(
            (User.username == form.username.data) |
            (User.email == form.email.data)
        ).first()

        if existing_user:
            if existing_user.username == form.username.data:
                flash("Username is already taken. Please choose a different one.", 'error')
            if existing_user.email == form.email.data:
                flash("Email is already registered. Please use a different email address.", 'error')
        else:
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
        # the URL included a full URL that inclused a domain name then the URL (netloc) is ignored (for security) and redirected to the index page 
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

# Define allowed file extensions and maximum file size
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
MAX_FILESIZE_MB = 8  # Maximum file size in megabytes

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/profile", methods=["GET", "POST"])
@login_required
def profile():
    form = ProfileForm()
    filenames = current_user.profile_picture or []
    print(f"Reading filenames stored in db: {filenames}")

    if form.validate_on_submit():
        # Handle image deletion
        if 'delete_picture' in request.form:
            picture_to_delete = request.form['delete_picture']
            if picture_to_delete in filenames:
                try:
                    os.remove(os.path.join(app.config['UPLOAD_PATH'], picture_to_delete))
                    print(f"Deleted file: {picture_to_delete}")
                except Exception as e:
                    print(f"Error deleting file: {e}")
                filenames.remove(picture_to_delete)
                current_user.profile_picture = filenames
                flag_modified(current_user, "profile_picture")
                db.session.commit()
                flash('Profile picture deleted successfully!', 'success')
                return redirect(url_for('profile'))

        # Handle file uploads
        if 'profile_picture' in request.files:
            files = request.files.getlist('profile_picture')
            for file in files:
                if file and allowed_file(file.filename):
                    # Generate a unique 32-character base64 filename
                    while True:
                        random_bytes = os.urandom(24)
                        random_filename = base64.urlsafe_b64encode(random_bytes).decode('utf-8')[:32]

                        # Ensure the filename has the correct extension
                        ext = os.path.splitext(file.filename)[1]
                        filename = secure_filename(random_filename + ext)
                        file_path = os.path.join(app.config['UPLOAD_PATH'], filename)

                        # Check if the filename already exists in the directory
                        if not os.path.exists(file_path):
                            break  # Exit the loop if the filename is unique

                    # Save the file and append the filename to the list
                    print(f"Saving file to: {file_path}")
                    file.save(file_path)
                    print(f"Filename appended to filenames: {filename}")
                    filenames.append(filename)
                    print(f"Filenames list: {filenames}")
                else:
                    flash(f"Invalid file type for {file.filename}. Only {', '.join(ALLOWED_EXTENSIONS)} allowed.", 'error')
                    return redirect(url_for('profile'))

            # Update user profile pictures in the database
            current_user.profile_picture = filenames
            flag_modified(current_user, "profile_picture")
            print(f"Updated user profile pictures in the DB: {current_user.profile_picture}")

        # Update other profile information
        current_user.bio = form.bio.data
        current_user.religion = form.religion.data
        current_user.politics = form.politics.data
        current_user.handling_money = form.handling_money.data
        current_user.health_living_space_cleanliness = form.health_living_space_cleanliness.data
        current_user.health_showering_frequency = form.health_showering_frequency.data
        current_user.health_oral_care = form.health_oral_care.data
        current_user.health_smoking = form.health_smoking.data
        current_user.health_alchohol_consumption = form.health_alchohol_consumption.data
        current_user.health_marijuana_consumption = form.health_marijuana_consumption.data

        # Commit changes to the database
        db.session.commit()
        print(f"Committed to DB: {current_user.profile_picture}")

        flash('Profile updated successfully!', 'success')
        return redirect(url_for('profile'))

    else:
        # Populate form with current user data
        form.bio.data = current_user.bio
        form.religion.data = current_user.religion
        form.politics.data = current_user.politics or []
        form.handling_money.data = current_user.handling_money or []
        form.health_living_space_cleanliness.data = current_user.health_living_space_cleanliness
        form.health_showering_frequency.data = current_user.health_showering_frequency
        form.health_oral_care.data = current_user.health_oral_care
        form.health_smoking.data = current_user.health_smoking
        form.health_alchohol_consumption.data = current_user.health_alchohol_consumption
        form.health_marijuana_consumption.data = current_user.health_marijuana_consumption

    return render_template("profile.html", title="Profile", form=form)



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
