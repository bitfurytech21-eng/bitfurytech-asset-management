from extensions import db


class BoardMember(db.Model):
    __tablename__ = "board_members"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(120))

    position = db.Column(db.String(120))

    image = db.Column(db.String(255))

    bio = db.Column(db.Text)

    linkedin = db.Column(db.String(255))

    display_order = db.Column(
        db.Integer,
        default=1
    )