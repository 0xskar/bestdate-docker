from datetime import datetime
from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db

class User(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True)
    email: so.Mapped[str] = so.mapped_column(sa.String(120), index=True, unique=True)
    password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))
    
    # Basic Information
    first_name: so.Mapped[str] = so.mapped_column(sa.String(64))
    last_name: so.Mapped[str] = so.mapped_column(sa.String(64))
    profile_picture: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))

    # Personal Details
    date_of_birth: so.Mapped[datetime] = so.mapped_column()
    gender: so.Mapped[str] = so.mapped_column(sa.String(32))
    gender_preference: so.Mapped[str] = so.mapped_column(sa.String(32))
    location: so.Mapped[str] = so.mapped_column(sa.String(128))
    bio: so.Mapped[Optional[str]] = so.mapped_column(sa.Text)

    # Preferences
    religion: so.Mapped[str] = so.mapped_column(sa.String(64))
    politics: so.Mapped[str] = so.mapped_column(sa.String(64))
    handling_money: so.Mapped[str] = so.mapped_column(sa.String(64))
    hygiene: so.Mapped[str] = so.mapped_column(sa.String(64))
    lifestyle_choices: so.Mapped[str] = so.mapped_column(sa.String(64))

    # Match Criteria
    religion_preference: so.Mapped[str] = so.mapped_column(sa.String(64))
    politics_preference: so.Mapped[str] = so.mapped_column(sa.String(64))
    handling_money_preference: so.Mapped[str] = so.mapped_column(sa.String(64))
    hygiene_preference: so.Mapped[str] = so.mapped_column(sa.String(64))
    lifestyle_choices_preference: so.Mapped[str] = so.mapped_column(sa.String(64))

    # Weighting Preferences
    religion_weight: so.Mapped[int] = so.mapped_column(sa.Integer)
    politics_weight: so.Mapped[int] = so.mapped_column(sa.Integer)
    handling_money_weight: so.Mapped[int] = so.mapped_column(sa.Integer)
    hygiene_weight: so.Mapped[int] = so.mapped_column(sa.Integer)
    lifestyle_choices_weight: so.Mapped[int] = so.mapped_column(sa.Integer)

    # Activity
    last_login: so.Mapped[datetime] = so.mapped_column()
    account_created: so.Mapped[datetime] = so.mapped_column(default=datetime.now)
    matches: so.Mapped[Optional[int]] = so.mapped_column(sa.Integer, default=0)
    messages_sent: so.Mapped[Optional[int]] = so.mapped_column(sa.Integer, default=0)
    messages_received: so.Mapped[Optional[int]] = so.mapped_column(sa.Integer, default=0)

    # Social Login
    google_id: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))
    facebook_id: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))

    # Other
    account_status: so.Mapped[str] = so.mapped_column(sa.String(32), default='active')
    subscription_type: so.Mapped[str] = so.mapped_column(sa.String(32), default='free')

    def __repr__(self):
        return '<User {}>'.format(self.username)
    