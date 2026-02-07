from models.citizen import Citizen
from flask import render_template, request

def citizen_list():
    if request.method == "POST":
        Citizen.create(request.form)
    citizens = Citizen.get_all()
    return render_template("citizens.html", citizens=citizens)