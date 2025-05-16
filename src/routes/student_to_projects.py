from flask import Flask, request, jsonify
from controllers.student_to_projects_controller import match_student_to_projects_controller

app = Flask(__name__)

@app.route("/v1/match/student-to-projects", methods=["POST"])
def match_student_to_projects():
    
    data = request.json
    
    if not data:
        return jsonify({"error": "Invalid request data"}), 400
    
    return match_student_to_projects_controller(data)