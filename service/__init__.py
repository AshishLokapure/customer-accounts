"""
Customer Accounts service package.
"""

import os

from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_talisman import Talisman

db = SQLAlchemy()


def create_app():
    """Create and configure the Flask application."""
    app = Flask(__name__)

    database_uri = os.getenv(
        "DATABASE_URI",
        "sqlite:///accounts.db"
    )

    app.config["SQLALCHEMY_DATABASE_URI"] = database_uri
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Initialize the database
    db.init_app(app)

    # Configure Cross-Origin Resource Sharing
    CORS(app)

    # Configure HTTP security headers with Flask-Talisman
    talisman = Talisman(app)
    app.extensions["talisman"] = talisman

    # Register account API routes
    from service.routes import accounts_bp
    app.register_blueprint(accounts_bp)

    # Create database tables if they do not exist
    with app.app_context():
        db.create_all()

    return app


app = create_app()
