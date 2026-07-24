from datetime import datetime
from extensions import db


class Investment(db.Model):
    __tablename__ = "investments"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    plan_name = db.Column(db.String(100), nullable=False)

    category = db.Column(db.String(50), nullable=False)

    amount = db.Column(db.Float, nullable=False)

    roi = db.Column(db.Float, nullable=False)

    duration = db.Column(db.Integer, nullable=False)

    status = db.Column(
        db.String(20),
        default="Running"
    )

    expected_return = db.Column(db.Float)

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    end_date = db.Column(db.DateTime)

    user = db.relationship(
        "User",
        backref="investments"
    )

    def to_dict(self):
        return {
            "id": self.id,
            "plan_name": self.plan_name,
            "category": self.category,
            "amount": self.amount,
            "roi": self.roi,
            "duration": self.duration,
            "status": self.status,
            "expected_return": self.expected_return,
            "created_at": self.created_at.isoformat(),
            "end_date": self.end_date.isoformat() if self.end_date else None
        }
