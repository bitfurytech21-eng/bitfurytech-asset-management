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


@board_bp.route("/board-member/<int:member_id>", methods=["GET"])
def get_board_member(member_id):

    member = BoardMember.query.get(member_id)

    if not member:
        return jsonify({
            "success": False,
            "message": "Board member not found."
        }), 404

    return jsonify({
        "success": True,
        "member": member.to_dict()
    })
