from datetime import datetime
from extensions import db


class Transaction(db.Model):
    __tablename__ = "transactions"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id")
    )

    transaction_type = db.Column(db.String(50))

    amount = db.Column(db.Float)

    wallet = db.Column(db.String(80))

    tx_hash = db.Column(db.String(255))

    status = db.Column(db.String(50))

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )