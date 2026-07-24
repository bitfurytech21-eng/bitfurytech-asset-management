from flask import Blueprint, jsonify
from models.transaction import Transaction

transaction_bp = Blueprint("transaction", __name__)


@transaction_bp.route("/transactions", methods=["GET"])
def get_transactions():

    transactions = Transaction.query.order_by(
        Transaction.created_at.desc()
    ).all()

    return jsonify({
        "success": True,
        "count": len(transactions),
        "transactions": [
            transaction.to_dict()
            for transaction in transactions
        ]
    })


@transaction_bp.route("/transaction/<int:transaction_id>", methods=["GET"])
def get_transaction(transaction_id):

    transaction = Transaction.query.get(transaction_id)

    if not transaction:
        return jsonify({
            "success": False,
            "message": "Transaction not found."
        }), 404

    return jsonify({
        "success": True,
        "transaction": transaction.to_dict()
    })
