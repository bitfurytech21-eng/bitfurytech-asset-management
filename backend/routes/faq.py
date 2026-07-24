from flask import Blueprint, jsonify
from models.faq import FAQ

faq_bp = Blueprint("faq", __name__)


@faq_bp.route("/faqs", methods=["GET"])
def get_faqs():

    faqs = FAQ.query.filter_by(
        is_active=True
    ).order_by(
        FAQ.display_order
    ).all()

    return jsonify({
        "success": True,
        "count": len(faqs),
        "faqs": [
            faq.to_dict()
            for faq in faqs
        ]
    })


@faq_bp.route("/faq/<int:faq_id>", methods=["GET"])
def get_faq(faq_id):

    faq = FAQ.query.get(faq_id)

    if not faq:
        return jsonify({
            "success": False,
            "message": "FAQ not found."
        }), 404

    return jsonify({
        "success": True,
        "faq": faq.to_dict()
    })
