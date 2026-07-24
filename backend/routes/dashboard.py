from flask import Blueprint, jsonify
from models.user import User
from models.investment import Investment
from models.transaction import Transaction

dashboard_bp = Blueprint("dashboard", __name__)


@dashboard_bp.route("/dashboard", methods=["GET"])
def dashboard():

    user = User.query.first()

    if not user:
        return jsonify({
            "success": False,
            "message": "No user found."
        }), 404

    total_portfolio = user.total_invested + user.total_profit

    active_investments = Investment.query.filter_by(
        user_id=user.id,
        status="Running"
    ).count()

    recent_transactions = Transaction.query.filter_by(
        user_id=user.id
    ).order_by(
        Transaction.created_at.desc()
    ).limit(5).all()

    return jsonify({

        "success": True,

        "user": {
            "name": user.full_name,
            "email": user.email,
            "country": user.country,
            "balance": user.account_balance,
            "total_invested": user.total_invested,
            "total_profit": user.total_profit,
            "portfolio": total_portfolio,
            "profile_image": user.profile_image
        },

        "summary": {
            "active_investments": active_investments
        },

        "transactions": [
            transaction.to_dict()
            for transaction in recent_transactions
        ]
    })
