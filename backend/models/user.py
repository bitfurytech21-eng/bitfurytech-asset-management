from datetime import datetime
from extensions import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(20))
    country = db.Column(db.String(100))
    profile_image = db.Column(db.String(255), default="default.png")

    account_balance = db.Column(db.Float, default=0.0)
    total_invested = db.Column(db.Float, default=0.0)
    total_profit = db.Column(db.Float, default=0.0)

    referral_code = db.Column(db.String(50), unique=True)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "full_name": self.full_name,
            "email": self.email,
            "phone": self.phone,
            "country": self.country,
            "profile_image": self.profile_image,
            "account_balance": self.account_balance,
            "total_invested": self.total_invested,
            "total_profit": self.total_profit,
            "referral_code": self.referral_code,
            "created_at": self.created_at.isoformat(),
        }
