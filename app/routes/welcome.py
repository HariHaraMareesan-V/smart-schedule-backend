from flask import Blueprint

welcome_bp = Blueprint("welcome", __name__)

@welcome_bp.route("/", methods=["GET"])
def home():
    return "<h2>Smart Schedule Backend is Running</h2>"
