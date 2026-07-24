from flask import Blueprint, jsonify

market_bp = Blueprint("market", __name__)

@market_bp.route("/api/market-overview", methods=["GET"])
def market():

    return jsonify({
        "widget": "TradingView",
        "status": "enabled"
    })