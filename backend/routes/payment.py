from flask import Blueprint, jsonify

payment_bp = Blueprint("payment", __name__)

@payment_bp.route("/api/payment-methods", methods=["GET"])
def payment_methods():

    return jsonify([
        {
            "coin": "Bitcoin",
            "symbol": "BTC",
            "network": "Bitcoin",
            "wallet": "YOUR_BTC_WALLET"
        },
        {
            "coin": "Ethereum",
            "symbol": "ETH",
            "network": "ERC20",
            "wallet": "YOUR_ETH_WALLET"
        },
        {
            "coin": "USDT",
            "symbol": "USDT",
            "network": "TRC20",
            "wallet": "YOUR_USDT_WALLET"
        },
        {
            "coin": "BNB",
            "symbol": "BNB",
            "network": "BEP20",
            "wallet": "YOUR_BNB_WALLET"
        },
        {
            "coin": "XRP",
            "symbol": "XRP",
            "network": "Ripple",
            "wallet": "YOUR_XRP_WALLET"
        }
    ])