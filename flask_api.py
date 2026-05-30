#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Flask API 服务器 — JSON-only 后端服务"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from flask import Flask
from flask_cors import CORS
from src.api.routes import api_bp


def create_app():
    app = Flask(__name__)
    CORS(app)
    app.secret_key = _get_secret_key()
    app.config["SESSION_PERMANENT"] = True
    app.config["PERMANENT_SESSION_LIFETIME"] = 86400

    app.register_blueprint(api_bp)

    @app.route("/api/health")
    def health():
        return {"success": True, "message": "LifeMonster API is running"}

    return app


def _get_secret_key():
    key_file = os.path.join(os.path.dirname(__file__), "config", "secret_key.txt")
    try:
        if os.path.exists(key_file):
            with open(key_file, "r") as f:
                return f.read().strip()
    except Exception:
        pass
    import secrets
    key = secrets.token_hex(32)
    try:
        os.makedirs(os.path.dirname(key_file), exist_ok=True)
        with open(key_file, "w") as f:
            f.write(key)
    except Exception:
        pass
    return key


app = create_app()

if __name__ == "__main__":
    print("LifeMonster API 服务启动中...")
    print("地址: http://127.0.0.1:5000")
    app.run(host="127.0.0.1", port=5000, debug=False, use_reloader=False)
