from flask import Blueprint, jsonify, session

notification_bp = Blueprint("notification", __name__)

@notification_bp.route("/api/notifications", methods=["GET"])
def notifications():

    if "user" not in session:
        return jsonify([]), 401

    return jsonify([
        {
            "title": "Deposit Confirmed",
            "message": "Your deposit has been confirmed."
        },
        {
            "title": "Investment Running",
            "message": "Your investment is earning daily returns."
        },
        {
            "title": "Security",
            "message": "Your account is protected by two-factor authentication."
        }
    ])