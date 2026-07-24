from flask import Blueprint, jsonify
from models.user import User

profile_bp = Blueprint("profile", __name__)


@profile_bp.route("/profile", methods=["GET"])
def profile():

    user = User.query.first()

    if not user:
        return jsonify({
            "success": False,
            "message": "User not found."
        }), 404

    return jsonify({

        "success": True,

        "profile": {

            "id": user.id,
            "full_name": user.full_name,
            "email": user.email,
            "phone": user.phone,
            "country": user.country,
            "profile_image": user.profile_image,
            "account_balance": user.account_balance,
            "total_invested": user.total_invested,
            "total_profit": user.total_profit,
            "referral_code": user.referral_code,
            "created_at": user.created_at

        }

    })
