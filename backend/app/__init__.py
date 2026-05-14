"""
Flask application initialization
"""

from flask import Flask
from flask_cors import CORS

def init_app(app):
    """Initialize Flask application"""
    
    # CORS configuration
    CORS(
        app,
        resources={
            r"/api/*": {
                "origins": ["http://localhost:3000", "http://localhost:3001"],
                "allow_headers": ["Content-Type", "Authorization"],
                "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
                "supports_credentials": True
            }
        }
    )
