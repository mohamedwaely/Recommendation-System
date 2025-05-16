from flask import Flask
import os
import sys

# Add the current directory to the Python path to make imports work
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from routes.projects_to_students import app as project_to_students_app
from routes.student_to_projects import app as student_to_projects_app
from controllers.student_to_projects_controller import match_student_to_projects_controller

app = Flask(__name__)

# Register routes from the imported modules
app.route("/v1/match/projects-to-students", methods=["POST"])(project_to_students_app.view_functions['match_project_to_students'])
app.route("/v1/match/student-to-projects", methods=["POST"])(student_to_projects_app.view_functions['match_student_to_projects'])

# Fix the import in the student_to_projects.py route
student_to_projects_app.view_functions['match_student_to_projects'].__globals__['match_student_to_projects_controller'] = match_student_to_projects_controller

@app.route('/')
def index():
    """Root route that provides basic API information"""
    return {
        "message": "Welcome to the Project-Student Matching API",
        "endpoints": [
            {
                "path": "/v1/match/projects-to-students",
                "method": "POST",
                "description": "Match a project to the most suitable students"
            },
            {
                "path": "/v1/match/student-to-projects",
                "method": "POST",
                "description": "Match a student to the most suitable projects"
            }
        ]
    }

from waitress import serve
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
    # serve(app, host="0.0.0.0", port=5000)