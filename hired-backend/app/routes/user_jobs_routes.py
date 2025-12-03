from flask import Blueprint, request, jsonify
from app.supabase_client import supabase

user_jobs_bp = Blueprint("user_jobs_bp", __name__)

@user_jobs_bp.route("/health", methods=["GET"])
def auth_health():
    return jsonify({"status": "User Job routes are working ✅"})
