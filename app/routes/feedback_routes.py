from flask import Blueprint, request, jsonify
from app import db
from app.models.feedback import Feedback
from flask_jwt_extended import jwt_required, get_jwt_identity

feedback_bp = Blueprint("feedback", __name__)

@feedback_bp.route("/submit", methods=["POST"])
@jwt_required()
def submit_feedback():
    data = request.get_json()
    user = get_jwt_identity()

    feedback = Feedback(
        user_id=user["id"],
        timetable_id=data["timetable_id"],
        rating=data["rating"],
        comment=data.get("comment", "")
    )
    db.session.add(feedback)
    db.session.commit()
    return jsonify({"message": "Feedback submitted"})
