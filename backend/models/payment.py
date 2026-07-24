from datetime import datetime
from extensions import db


class PaymentMethod(db.Model):
    __tablename__ = "payment_methods"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(50), nullable=False)

    symbol = db.Column(db.String(10), nullable=False)

    wallet_address = db.Column(db.String(255), nullable=False)

    network = db.Column(db.String(50), nullable=False)

    qr_code = db.Column(db.String(255))

    minimum_deposit = db.Column(db.Float, default=500.0)

    status = db.Column(db.String(20), default="Active")

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "symbol": self.symbol,
            "wallet_address": self.wallet_address,
            "network": self.network,
            "qr_code": self.qr_code,
            "minimum_deposit": self.minimum_deposit,
            "status": self.status
        }
