from flask import Blueprint, request, jsonify, session

auth_bp = Blueprint("auth", __name__)

# Temporary users (replace with database later)
users = {
    "admin@bitfurytechinvestment.com": {
        "password": "Admin123!",
        "name": "Administrator",
        "role": "admin"
    }
}


@auth_bp.route("/api/register", methods=["POST"])
def register():

    data = request.get_json()

    email = data.get("email", "").lower().strip()
    password = data.get("password", "")
    name = data.get("name", "")

    if email in users:
        return jsonify({
            "success": False,
            "message": "Email already exists."
        }), 409

    users[email] = {
        "password": password,
        "name": name,
        "role": "user"
    }

    return jsonify({
        "success": True,
        "message": "Registration successful."
    })


@auth_bp.route("/api/login", methods=["POST"])
def login():

    data = request.get_json()

    email = data.get("email", "").lower().strip()
    password = data.get("password", "")

    user = users.get(email)

    if not user or user["password"] != password:
        return jsonify({
            "success": False,
            "message": "Invalid email or password."
        }), 401

    session["user"] = {
        "email": email,
        "name": user["name"],
        "role": user["role"]
    }

    return jsonify({
        "success": True,
        "user": session["user"]
    })


@auth_bp.route("/api/logout")
def logout():

    session.clear()

    return jsonify({
        "success": True,
        "message": "Logged out successfully."
    })


@auth_bp.route("/api/me")
def me():

    if "user" not in session:
        return jsonify({
            "success": False,
            "message": "Not logged in."
        }), 401

    return jsonify(session["user"])