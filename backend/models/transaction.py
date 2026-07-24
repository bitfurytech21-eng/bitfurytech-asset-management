from datetime import datetime
from extensions import db


class Transaction(db.Model):
    __tablename__ = "transactions"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    transaction_type = db.Column(
        db.String(30),
        nullable=False
    )

    amount = db.Column(
        db.Float,
        nullable=False
    )

    currency = db.Column(
        db.String(10),
        default="USD"
    )

    payment_method = db.Column(
        db.String(50)
    )

    status = db.Column(
        db.String(20),
        default="Pending"
    )

    reference = db.Column(
        db.String(100),
        unique=True
    )

    description = db.Column(
        db.Text
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    user = db.relationship(
        "User",
        backref="transactions"
    )

    def to_dict(self):
        return {
            "id": self.id,
            "transaction_type": self.transaction_type,
            "amount": self.amount,
            "currency": self.currency,
            "payment_method": self.payment_method,
            "status": self.status,
            "reference": self.reference,
            "description": self.description,
            "created_at": self.created_at.isoformat()
        }
