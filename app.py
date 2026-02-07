from flask import Flask
from controllers.cntr_citizen import citizen_list
from controllers.cntr_assignment import process_assignments

app = Flask(__name__)

app.add_url_rule("/citizens", view_func=citizen_list, methods=["GET", "POST"])
app.add_url_rule("/assignments", view_func=process_assignments)

app.run(debug=True)