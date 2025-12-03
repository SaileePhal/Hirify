from flask import Blueprint, request, jsonify
from app.supabase_client import supabase

auth_bp = Blueprint("auth_bp", __name__)

@auth_bp.route("/health", methods=["GET"])
def auth_health():
    return jsonify({"status": "Auth routes are working ✅"})
