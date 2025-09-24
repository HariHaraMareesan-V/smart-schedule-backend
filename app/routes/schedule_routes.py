from flask import Blueprint, jsonify
from app.models.optimization import generate_schedule

schedule_bp = Blueprint("schedule", __name__)

@schedule_bp.route("/generate", methods=["GET"])
def generate():
    # Dummy data for now
    subjects = [{"id": 1}, {"id": 2}, {"id": 3}]
    rooms = [{"id": 101}, {"id": 102}]
    faculty_availability = {}

    result = generate_schedule(subjects, rooms, faculty_availability)
    return jsonify(result)
