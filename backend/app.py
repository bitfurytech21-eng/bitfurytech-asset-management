from flask import Flask
from config import Config
from extensions import db, bcrypt, migrate, cors

# Import all models
from models import *

# Import all blueprints
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
    app = Flask(__name__)

    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db)
    cors.init_app(app)

    # Register blueprints
    app.register_blueprint(auth_bp, url_prefix="/api")
    app.register_blueprint(dashboard_bp, url_prefix="/api")
    app.register_blueprint(profile_bp, url_prefix="/api")
    app.register_blueprint(investment_bp, url_prefix="/api")
    app.register_blueprint(transaction_bp, url_prefix="/api")
    app.register_blueprint(notification_bp, url_prefix="/api")
    app.register_blueprint(board_bp, url_prefix="/api")
    app.register_blueprint(payment_bp, url_prefix="/api")
    app.register_blueprint(market_bp, url_prefix="/api")
    app.register_blueprint(faq_bp, url_prefix="/api")

    @app.route("/")
    def home():
        return {
            "application": "Bitfury Tech Investment API",
            "status": "Running",
            "version": "1.0.0"
        }

    with app.app_context():
        db.create_all()

    return app


app = create_app()

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
