from flask import Blueprint, jsonify, session

transaction_bp = Blueprint("transaction", __name__)

@transaction_bp.route("/api/transactions", methods=["GET"])
def transactions():

    if "user" not in session:
        return jsonify([]), 401

    return jsonify([
        {
            "id": 1,
            "type": "Deposit",
            "amount": 5000,
            "status": "Completed",
            "date": "2026-07-23"
        },
        {
            "id": 2,
            "type": "Investment",
            "amount": 2500,
            "status": "Running",
            "date": "2026-07-22"
        },
        {
            "id": 3,
            "type": "Withdrawal",
            "amount": 800,
            "status": "Pending",
            "date": "2026-07-21"
        }
    ])