from flask import Blueprint, jsonify

board_bp = Blueprint("board", __name__)

@board_bp.route("/api/board-members", methods=["GET"])
def board():

    return jsonify([
        {
            "id": 1,
            "name": "John Smith",
            "position": "Chief Executive Officer",
            "image": "/images/board/ceo.jpg",
            "bio": "25 years investment management."
        },
        {
            "id": 2,
            "name": "Jane Williams",
            "position": "Chief Financial Officer",
            "image": "/images/board/cfo.jpg",
            "bio": "Corporate finance specialist."
        }
    ])