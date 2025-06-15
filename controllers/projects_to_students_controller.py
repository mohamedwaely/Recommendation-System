from flask import jsonify
from services.tf_idf_similarity_service import projects_to_students_similarity_service

def match_project_to_students_controller(data):
    top_n = int(5)
    
    project = data.get("project", {})
    if not project:
        return jsonify({"error": "Project data is required"}), 400
    
    project_title = project.get("title", "")
    project_skills = project.get("skills", "")
    
    # Get students data from the request
    students_data = data.get("students", [])
    if not students_data:
        return jsonify({"error": "Students data is required"}), 400
    
    # Create a requirement text from the project data (title and skills only)
    project_requirements = f"{project_title} {project_skills}"
    
    # Get all student texts (jobtitle and skills only)
    student_texts = []
    for student in students_data:
        student_text = f"{student.get('jobtitle', '')} {student.get('skills', '')}"
        student_texts.append(student_text)
    
    # Fixed: Swap parameter order to match service implementation
    return projects_to_students_similarity_service(project_requirements, student_texts, top_n, students_data)