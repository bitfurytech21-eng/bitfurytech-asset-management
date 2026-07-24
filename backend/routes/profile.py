from flask import Blueprint, jsonify, session

profile_bp = Blueprint("profile", __name__)

@profile_bp.route("/api/profile", methods=["GET"])
def profile():

    if "user" not in session:
        return jsonify({
            "success": False,
            "message": "Unauthorized"
        }), 401

    return jsonify({
        "success": True,
        "name": session["user"]["name"],
        "email": session["user"]["email"],
        "country": "Australia",
        "phone": "+61 400 000 000",
        "status": "Verified",
        "kyc": "Completed",
        "photo": "/images/default-avatar.png"
    })