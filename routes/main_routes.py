# routes/main_routes.py
from flask import Blueprint, jsonify

main_bp = Blueprint('main', __name__)

@main_bp.route('/api/health')
def health():
    return jsonify({"ok": True})
