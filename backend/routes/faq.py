from flask import Blueprint, jsonify

faq_bp = Blueprint("faq", __name__)

@faq_bp.route("/api/faqs", methods=["GET"])
def faqs():

    return jsonify([
        {
            "question": "What is the minimum investment?",
            "answer": "$500."
        },
        {
            "question": "How do I withdraw?",
            "answer": "Submit a withdrawal request from your dashboard."
        },
        {
            "question": "Which cryptocurrencies are supported?",
            "answer": "BTC, ETH, USDT, BNB and XRP."
        }
    ])