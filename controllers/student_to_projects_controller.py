from flask import jsonify
from services.tf_idf_similarity_service import student_to_projects_similarity_service

def match_student_to_projects_controller(data):
    top_n = int(5)

    student = data.get("student", {})
    if not student:
        return jsonify({"error": "Student data is required"}), 400
    
    student_jobtitle = student.get("jobtitle", "")
    student_skills = student.get("skills", "")
    
    # Get projects data from the request
    projects_data = data.get("projects", [])
    if not projects_data:
        return jsonify({"error": "Projects data is required"}), 400

    
    # Create a profile text from the student data (jobtitle and skills only)
    student_profile = f"{student_jobtitle} {student_skills}"
    
    # Get all project texts (title and skills only)
    project_texts = []
    for project in projects_data:
        project_text = f"{project.get('title', '')} {project.get('skills', '')}"
        project_texts.append(project_text)

    return student_to_projects_similarity_service(student_profile, project_texts, top_n, projects_data)

