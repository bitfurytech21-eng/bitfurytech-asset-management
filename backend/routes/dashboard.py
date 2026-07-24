from flask import Blueprint, jsonify, session

dashboard_bp = Blueprint("dashboard", __name__)

@dashboard_bp.route("/api/dashboard", methods=["GET"])
def dashboard():

    if "user" not in session:
        return jsonify({
            "success": False,
            "message": "Unauthorized"
        }), 401

    return jsonify({
        "success": True,
        "portfolio": 25000,
        "balance": 8200,
        "interest": 730,
        "total_invested": 18500,
        "withdrawals": 4200,
        "referrals": 15
    })