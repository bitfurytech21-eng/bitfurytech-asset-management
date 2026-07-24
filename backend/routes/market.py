from flask import Blueprint, jsonify

market_bp = Blueprint("market", __name__)


@market_bp.route("/market", methods=["GET"])
def get_market():

    return jsonify({
        "success": True,
        "market": [
            {
                "symbol": "BTC/USD",
                "name": "Bitcoin",
                "price": 118500.25,
                "change": "+2.85%"
            },
            {
                "symbol": "ETH/USD",
                "name": "Ethereum",
                "price": 3750.80,
                "change": "+1.42%"
            },
            {
                "symbol": "XRP/USD",
                "name": "Ripple",
                "price": 0.91,
                "change": "-0.53%"
            },
            {
                "symbol": "SPX",
                "name": "S&P 500",
                "price": 6450.32,
                "change": "+0.88%"
            },
            {
                "symbol": "XAU/USD",
                "name": "Gold",
                "price": 2458.60,
                "change": "+0.31%"
            }
        ]
    })
