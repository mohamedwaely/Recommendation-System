from flask import request, jsonify
from controllers.projects_to_students_controller import match_project_to_students_controller
from flask import Flask

app = Flask(__name__)

@app.route("/v1/match/projects-to-students", methods=["POST"])
def match_project_to_students():
    
    data = request.json
    
    if not data:
        return jsonify({"error": "Invalid request data"}), 400
    
    return match_project_to_students_controller(data)
    
