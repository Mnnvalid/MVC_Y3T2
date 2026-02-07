from models.models_assignments import Assignment
from models.database import get_db

def process_assignment_gui():
    db = get_db()
    citizens = db.execute("SELECT * FROM citizens").fetchall()
    citizens.sort(key=lambda c: c[2])

    for c in citizens:
        Assignment.assign(c)

    report = db.execute("""
        SELECT c.*, a.shelter_id
        FROM citizens c
        LEFT JOIN assignments a
        ON c.citizen_id = a.citizen_id
    """).fetchall()

    return report
