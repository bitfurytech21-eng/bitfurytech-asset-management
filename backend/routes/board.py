from flask import Blueprint, jsonify
from models.board import BoardMember

board_bp = Blueprint("board", __name__)


@board_bp.route("/board-members", methods=["GET"])
def get_board_members():

    members = BoardMember.query.filter_by(
        is_active=True
    ).order_by(
        BoardMember.display_order
    ).all()

    return jsonify({
        "success": True,
        "count": len(members),
        "members": [
            member.to_dict()
            for member in members
        ]
    })


@app.route("/api/board-members/<int:id>")
def get_board_member(id):

    board = {
        1: {
            "id": 1,
            "name": "John Smith",
            "position": "Chairman",
            "biography": "John Smith has over 30 years of experience in investment management and corporate governance."
        },
        2: {
            "id": 2,
            "name": "Sarah Williams",
            "position": "Chief Executive Officer",
            "biography": "Sarah Williams leads Bitfury Tech Investment with extensive expertise in financial markets and technology."
        },
        3: {
            "id": 3,
            "name": "Michael Johnson",
            "position": "Chief Financial Officer",
            "biography": "Michael Johnson oversees the company's financial strategy, compliance, and investor reporting."
        }
    }

    if id not in board:
        return jsonify({"message": "Board member not found"}), 404

    return jsonify(board[id])
