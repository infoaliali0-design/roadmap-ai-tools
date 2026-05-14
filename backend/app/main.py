# -*- coding: utf-8 -*-
"""
Flask application setup and configuration
"""

import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime

from app.config import config

app = Flask(__name__)

# Load configuration
env = os.getenv('FLASK_ENV', 'development')
app.config.from_object(config.get(env, config['development']))

# Enable CORS
CORS(
    app,
    resources={
        r"/api/*": {
            "origins": os.getenv('CORS_ORIGINS', 'http://localhost:3000').split(','),
            "allow_headers": ["Content-Type", "Authorization"],
            "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
            "supports_credentials": True
        }
    }
)

# Health Check Endpoint
@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'service': 'Roadmap AI Tools API',
        'version': '1.0.0',
        'timestamp': datetime.utcnow().isoformat()
    }), 200

# Error Handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({
        'status': 'error',
        'message': 'Resource not found',
        'error': 'NOT_FOUND'
    }), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({
        'status': 'error',
        'message': 'Internal server error',
        'error': 'INTERNAL_ERROR'
    }), 500

@app.errorhandler(403)
def forbidden(error):
    return jsonify({
        'status': 'error',
        'message': 'Forbidden',
        'error': 'FORBIDDEN'
    }), 403

@app.errorhandler(400)
def bad_request(error):
    return jsonify({
        'status': 'error',
        'message': 'Bad request',
        'error': 'BAD_REQUEST'
    }), 400

if __name__ == '__main__':
    app.run(debug=True)
