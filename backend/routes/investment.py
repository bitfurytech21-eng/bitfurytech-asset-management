from flask import Blueprint, jsonify

investment_bp = Blueprint("investment", __name__)

@investment_bp.route("/api/plans", methods=["GET"])
def plans():

    return jsonify([
        {
            "title": "Real Estate",
            "minimum": 500,
            "roi": "8%",
            "duration": 30
        },
        {
            "title": "Agriculture",
            "minimum": 500,
            "roi": "7%",
            "duration": 30
        },
        {
            "title": "Stocks",
            "minimum": 500,
            "roi": "9%",
            "duration": 30
        },
        {
            "title": "Crypto",
            "minimum": 500,
            "roi": "10%",
            "duration": 30
        }
    ])