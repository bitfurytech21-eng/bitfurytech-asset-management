from extensions import db


class Investment(db.Model):
    __tablename__ = "investment_plans"

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(100), nullable=False)

    category = db.Column(db.String(80))

    description = db.Column(db.Text)

    minimum = db.Column(db.Float)

    maximum = db.Column(db.Float)

    daily_roi = db.Column(db.Float)

    duration = db.Column(db.Integer)

    image = db.Column(db.String(255))

    status = db.Column(
        db.String(20),
        default="Active"
    )