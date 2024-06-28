from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from typing import Optional, List
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db, login
from flask_login import UserMixin
import json

# JSON encoding to store certain fields as lists
class JSONEncodedList(sa.types.TypeDecorator):
    impl = sa.String

    def process_bind_param(self, value, dialect):
        if value is None:
            return '[]'
        return json.dumps(value)

    def process_result_value(self, value, dialect):
        if value is None:
            return []
        return json.loads(value)

class User(UserMixin, db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True, nullable=False)
    email: so.Mapped[str] = so.mapped_column(sa.String(120), index=True, unique=True, nullable=False)
    password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))

    # Basic Information (registration)
    first_name: so.Mapped[str] = so.mapped_column(sa.String(64), nullable=False)
    last_name: so.Mapped[str] = so.mapped_column(sa.String(64), nullable=False)
    profile_picture: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))

    # Personal Details (registration)
    date_of_birth: so.Mapped[datetime] = so.mapped_column(nullable=False)
    gender: so.Mapped[str] = so.mapped_column(sa.String(32), nullable=False)
    location: so.Mapped[str] = so.mapped_column(sa.String(128), nullable=False)

    # Personal Details 
    bio: so.Mapped[Optional[str]] = so.mapped_column(sa.Text)
    religion: so.Mapped[Optional[str]] = so.mapped_column(sa.String(64))
    politics: so.Mapped[List[str]] = so.mapped_column(JSONEncodedList, nullable=False, default=[])
    handling_money: so.Mapped[List[str]] = so.mapped_column(JSONEncodedList, nullable=False, default=[])

    # Personal Health
    health_living_space_cleanliness: so.Mapped[Optional[str]] = so.mapped_column(sa.String(64))
    health_showering_frequency: so.Mapped[Optional[str]] = so.mapped_column(sa.String(64))
    health_oral_care: so.Mapped[Optional[str]] = so.mapped_column(sa.String(64))
    health_smoking: so.Mapped[Optional[str]] = so.mapped_column(sa.String(64))
    health_alchohol_consumption: so.Mapped[Optional[str]] = so.mapped_column(sa.String(64))
    health_marijuana_consumption: so.Mapped[Optional[str]] = so.mapped_column(sa.String(64))

    # Match Criteria
    gender_preference: so.Mapped[List[str]] = so.mapped_column(JSONEncodedList, nullable=False, default=[])
    religion_preference: so.Mapped[Optional[str]] = so.mapped_column(sa.String(64))
    politics_preference: so.Mapped[Optional[str]] = so.mapped_column(sa.String(64))
    handling_money_preference: so.Mapped[Optional[str]] = so.mapped_column(sa.String(64))

    # Match Health Preferences
    health_living_space_cleanliness_preference: so.Mapped[Optional[str]] = so.mapped_column(sa.String(64))
    health_showering_frequency_preference: so.Mapped[Optional[str]] = so.mapped_column(sa.String(64))
    health_oral_care_preference: so.Mapped[Optional[str]] = so.mapped_column(sa.String(64))
    health_smoking_preference: so.Mapped[Optional[str]] = so.mapped_column(sa.String(64))
    health_alchohol_consumption_preference: so.Mapped[Optional[str]] = so.mapped_column(sa.String(64))
    health_marijuana_consumption_preference: so.Mapped[Optional[str]] = so.mapped_column(sa.String(64))

    # Activity
    last_login: so.Mapped[datetime] = so.mapped_column(default=datetime.now, nullable=False)
    account_created: so.Mapped[datetime] = so.mapped_column(default=datetime.now, nullable=False)
    matches: so.Mapped[Optional[int]] = so.mapped_column(sa.Integer, default=0)
    messages_sent: so.Mapped[Optional[int]] = so.mapped_column(sa.Integer, default=0)
    messages_received: so.Mapped[Optional[int]] = so.mapped_column(sa.Integer, default=0)

    # Social Login
    google_id: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))
    facebook_id: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))

    # Other
    account_status: so.Mapped[str] = so.mapped_column(sa.String(32), default='active', nullable=False)
    subscription_type: so.Mapped[str] = so.mapped_column(sa.String(32), default='free', nullable=False)

    # werkzeug set/check password 
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)

    # get null fields to populate user profile form
    def get_null_fields(self):
        null_fields = []
        if not self.gender_preference:
            null_fields.append('gender_preference')
        if not self.bio:
            null_fields.append('bio')
        if not self.religion:
            null_fields.append('religion')
        if not self.politics:
            null_fields.append('politics')
        if not self.handling_money:
            null_fields.append('handling_money')
        if not self.health_showering_frequency:
            null_fields.append('health_showering_frequency')
        if not self.health_oral_care:
            null_fields.append('health_oral_care')
        if not self.health_smoking:
            null_fields.append('health_smoking')
        if not self.health_living_space_cleanliness:
            null_fields.append('health_living_space_cleanliness')
        if not self.religion_preference:
            null_fields.append('religion_preference')
        if not self.politics_preference:
            null_fields.append('politics_preference')
        if not self.handling_money_preference:
            null_fields.append('handling_money_preference')
        if not self.health_showering_frequency_preference:
            null_fields.append('health_showering_frequency_preference')
        if not self.health_oral_care_preference:
            null_fields.append('health_oral_care_preference')
        if not self.health_smoking_preference:
            null_fields.append('health_smoking_preference')
        if not self.health_living_space_cleanliness_preference:
            null_fields.append('health_living_space_cleanliness_preference')
        return null_fields

    # User loader function
    @login.user_loader
    def load_user(id):
        return db.session.get(User, int(id))
