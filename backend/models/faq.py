from extensions import db


class FAQ(db.Model):
    __tablename__ = "faqs"

    id = db.Column(db.Integer, primary_key=True)

    question = db.Column(db.Text)

    answer = db.Column(db.Text)

    category = db.Column(db.String(80))