from flask import Flask
from flask_cors import CORS

from config import Config
from extensions import db, bcrypt

# Import blueprints
from routes.auth import auth_bp
from routes.dashboard import dashboard_bp
from routes.profile import profile_bp
from routes.investment import investment_bp
from routes.transaction import transaction_bp
from routes.notification import notification_bp
from routes.board import board_bp
from routes.payment import payment_bp
from routes.market import market_bp
from routes.faq import faq_bp


def create_app():

    app = Flask(
        __name__,
        static_folder="static",
        static_url_path="/static"
    )

    app.config.from_object(Config)

    CORS(
        app,
        supports_credentials=True
    )

    db.init_app(app)
    bcrypt.init_app(app)

    with app.app_context():
        db.create_all()

    # Register Blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(profile_bp)
    app.register_blueprint(investment_bp)
    app.register_blueprint(transaction_bp)
    app.register_blueprint(notification_bp)
    app.register_blueprint(board_bp)
    app.register_blueprint(payment_bp)
    app.register_blueprint(market_bp)
    app.register_blueprint(faq_bp)

    @app.route("/")
    def home():
        return {
            "application": "Bitfury Tech Investment",
            "status": "Backend Running",
            "version": "1.0.0"
        }

    return app


app = create_app()

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )