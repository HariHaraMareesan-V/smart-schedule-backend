from app import db

class TimetableSlot(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject_id = db.Column(db.Integer, nullable=False)
    faculty_id = db.Column(db.Integer, nullable=False)
    room_id = db.Column(db.Integer, nullable=False)
    day = db.Column(db.String(10), nullable=False)  # e.g. Monday
    time = db.Column(db.String(10), nullable=False)  # e.g. 10:00 AM
