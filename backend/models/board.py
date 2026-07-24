from datetime import datetime
from extensions import db


class BoardMember(db.Model):
    __tablename__ = "board_members"

    id = db.Column(db.Integer, primary_key=True)

    full_name = db.Column(
        db.String(100),
        nullable=False
    )

    position = db.Column(
        db.String(100),
        nullable=False
    )

    biography = db.Column(
        db.Text,
        nullable=False
    )

    image = db.Column(
        db.String(255),
        nullable=False
    )

    linkedin = db.Column(
        db.String(255)
    )

    email = db.Column(
        db.String(120)
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
            "full_name": self.full_name,
            "position": self.position,
            "biography": self.biography,
            "image": self.image,
            "linkedin": self.linkedin,
            "email": self.email,
            "display_order": self.display_order,
            "is_active": self.is_active
        }
