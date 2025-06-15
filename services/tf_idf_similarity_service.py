from flask import jsonify
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from typing import List, Dict

def student_to_projects_similarity_service(student_profile: str, project_texts: List[str], top_n: int, projects_data: List[Dict]):
    
    all_texts = [student_profile] + project_texts
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(all_texts)
    
    student_vector = tfidf_matrix[0:1]
    project_vectors = tfidf_matrix[1:]
    
    # Calculate cosine similarities
    cosine_similarities = linear_kernel(student_vector, project_vectors).flatten()
    
    # Get top N project indices
    top_indices = cosine_similarities.argsort()[::-1][:top_n]
    
    # Build result with similarity scores
    results = []
    for idx in top_indices:
        project = projects_data[idx]
        results.append({
            "project_id": project.get("id", ""),
            "title": project.get("title", ""),
            "skills": project.get("skills", ""),
            "similarity_score": float(cosine_similarities[idx])
        })
    
    return jsonify({
        "matches": results,
        "total_projects": len(projects_data)
    })

def projects_to_students_similarity_service(project_requirements: str, student_texts: List[str], top_n: int, students_data: List[Dict]):

    all_texts = [project_requirements] + student_texts
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(all_texts)
    
    project_vector = tfidf_matrix[0:1]
    student_vectors = tfidf_matrix[1:]
    
    # Calculate cosine similarities
    cosine_similarities = linear_kernel(project_vector, student_vectors).flatten()
    
    # Get top N student indices
    top_indices = cosine_similarities.argsort()[::-1][:top_n]
    
    # Build result with similarity scores
    results = []
    for idx in top_indices:
        student = students_data[idx]
        results.append({
            "student_id": student.get("id", ""),
            "jobtitle": student.get("jobtitle", ""),
            "skills": student.get("skills", ""),
            "similarity_score": float(cosine_similarities[idx])
        })
    
    return jsonify({
        "matches": results,
        "total_students": len(students_data)
    })