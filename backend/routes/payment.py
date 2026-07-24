from flask import Blueprint, jsonify
from models.payment import PaymentMethod

payment_bp = Blueprint("payment", __name__)


@payment_bp.route("/payments", methods=["GET"])
def get_payment_methods():

    methods = PaymentMethod.query.filter_by(
        status="Active"
    ).all()

    return jsonify({
        "success": True,
        "count": len(methods),
        "payments": [
            method.to_dict()
            for method in methods
        ]
    })


@payment_bp.route("/payment/<int:payment_id>", methods=["GET"])
def get_payment_method(payment_id):

    method = PaymentMethod.query.get(payment_id)

    if not method:
        return jsonify({
            "success": False,
            "message": "Payment method not found."
        }), 404

    return jsonify({
        "success": True,
        "payment": method.to_dict()
    })
