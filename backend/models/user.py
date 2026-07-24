from extensions import db
from datetime import datetime


class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    full_name = db.Column(db.String(120), nullable=False)

    email = db.Column(db.String(120), unique=True, nullable=False)

    password = db.Column(db.String(255), nullable=False)

    role = db.Column(db.String(20), default="user")

    country = db.Column(db.String(100))

    phone = db.Column(db.String(50))

    photo = db.Column(
        db.String(255),
        default="/images/users/default-avatar.png"
    )

    wallet_balance = db.Column(db.Float, default=0)

    interest_balance = db.Column(db.Float, default=0)

    total_invested = db.Column(db.Float, default=0)

    kyc_status = db.Column(
        db.String(50),
        default="Pending"
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )