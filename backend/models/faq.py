from datetime import datetime
from extensions import db


class FAQ(db.Model):
    __tablename__ = "faqs"

    id = db.Column(db.Integer, primary_key=True)

    question = db.Column(
        db.String(255),
        nullable=False
    )

    answer = db.Column(
        db.Text,
        nullable=False
    )

    category = db.Column(
        db.String(100),
        default="General"
    )

    display_order = db.Column(
        db.Integer,
        default=1
    )

    is_active = db.Column(
        db.Boolean,
        default=True
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    def to_dict(self):
        return {
            "id": self.id,
            "question": self.question,
            "answer": self.answer,
            "category": self.category,
            "display_order": self.display_order,
            "is_active": self.is_active
        }
