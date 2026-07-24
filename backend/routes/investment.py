from flask import Blueprint, jsonify
from models.investment import Investment

investment_bp = Blueprint("investment", __name__)


@investment_bp.route("/investments", methods=["GET"])
def get_investments():

    investments = Investment.query.order_by(
        Investment.created_at.desc()
    ).all()

    return jsonify({
        "success": True,
        "count": len(investments),
        "investments": [
            investment.to_dict()
            for investment in investments
        ]
    })


@investment_bp.route("/investment/<int:investment_id>", methods=["GET"])
def get_investment(investment_id):

    investment = Investment.query.get(investment_id)

    if not investment:
        return jsonify({
            "success": False,
            "message": "Investment not found."
        }), 404

    return jsonify({
        "success": True,
        "investment": investment.to_dict()
    })
