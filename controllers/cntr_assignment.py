from models.models_citizen import Citizen
from models.models_assignments import Assignment
from flask import render_template

def process_assignments():
    citizens = Citizen.get_all()
    
    citizens.sort(key=lambda c: c[2])
    
    for c in citizens:
        Assignment.assign(c)
    
    return report_list()

def report_list():
    from models.database import get_db
    data = get_db().execute("""
        SELECT c.*, a.shelter_id
        FROM citizens c
        LEFT JOIN assignments a
        ON c.citizen_id = a.citizen_id
    """).fetchall()

    return render_template("report.html", data=data)