from extensions import db


class PaymentMethod(db.Model):
    __tablename__ = "payment_methods"

    id = db.Column(db.Integer, primary_key=True)

    coin = db.Column(db.String(50))

    network = db.Column(db.String(50))

    wallet_address = db.Column(db.Text)

    qr_code = db.Column(db.String(255))

    status = db.Column(
        db.String(30),
        default="Active"
    )