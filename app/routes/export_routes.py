from flask import Blueprint, Response
import csv
from io import StringIO

export_bp = Blueprint("export", __name__)

@export_bp.route("/timetable/csv", methods=["GET"])
def export_csv():
    output = StringIO()
    writer = csv.writer(output)
    writer.writerow(["Subject", "Faculty", "Room", "Day", "Time"])

    # Dummy data for now
    writer.writerow(["Math", "Dr. Rao", "101", "Monday", "10:00 AM"])
    writer.writerow(["Physics", "Ms. Iyer", "102", "Tuesday", "11:00 AM"])

    output.seek(0)
    return Response(output, mimetype="text/csv", headers={"Content-Disposition": "attachment; filename=timetable.csv"})
