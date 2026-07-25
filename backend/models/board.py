from extensions import db

class BoardMember(db.Model):
    __tablename__ = "board_members"

    id = db.Column(db.Integer, primary_key=True)

    biography = db.Column(db.Text, nullable=False)

    created_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )

    def to_dict(self):
        return {
            "id": self.id,
            "biography": self.biography,
        }