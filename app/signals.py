from datetime import datetime
from flask_login import user_logged_in
from app import db, app
from app.models import User

@user_logged_in.connect_via(app)
def when_user_logged_in(sender, user):
    user.last_login = datetime.now()
    db.session.commit()
