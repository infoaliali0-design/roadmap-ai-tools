#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Entry point for Roadmap AI Tools Flask application
"""

import os
import sys
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Add current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.main import app

if __name__ == '__main__':
    host = os.getenv('HOST', '0.0.0.0')
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('FLASK_ENV') == 'development'
    
    print(f"\n🚀 Starting Roadmap AI Tools API")
    print(f"📍 Server: http://{host}:{port}")
    print(f"🔧 Environment: {os.getenv('FLASK_ENV', 'development')}")
    print(f"\n✨ Ready to handle AI workflows and file conversions!\n")
    
    app.run(
        host=host,
        port=port,
        debug=debug,
        use_reloader=debug
    )
