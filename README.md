# Job-Project Recommendation System

A Flask-based recommendation system that matches students with relevant projects based on their skills and job profiles.

## Features
- Recommends projects to students based on their job title, and skills.
- Searches for students based on job title and skills
- Uses TF-IDF vectorization and cosine similarity for recommendations

## Project Structure

```
Recommendation-System/
├── requirements.txt
├── .gitignore
├── README.md
├── venv/
├── src/
├── main.py
│   ├── controllers/
│   │   ├── projects_to_students_controller.py
│   │   └── student_to_projects_controller.py
│   ├── routes/
│   │   ├── project_to_students.py
│   │   └── student_to_projects.py
│   └── services/
│       └── tf_idf_similarity_service.py
```

## Setup Instructions

1. Create a virtual environment (recommended):
   ```
   # Recommended to use conda
   conda create -n rsvenv python=3.13
   conda activate rsvenv
   
   # or
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   python main.py
   ```

## API Endpoints

### 1. Match Project to Students

- **URL**: `/v1/match/projects-to-students`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "project": {
      "id": "project_id",
      "title": "Project Title",
      "skills": "Required Skills"
    },
    "students": [
      {
        "id": "student_id",
        "jobtitle": "Student Job Title",
        "skills": "Student Skills"
      }
    ]
  }
  ```
- **Response**:
  ```json
  {
    "matches": [
      {
        "student_id": "student_id",
        "jobtitle": "Student Job Title",
        "skills": "Student Skills",
        "similarity_score": 0.75
      }
    ],
    "total_students": 1
  }
  ```

### 2. Match Student to Projects

- **URL**: `/v1/match/student-to-projects`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "student": {
      "id": "student_id",
      "jobtitle": "Student Job Title",
      "skills": "Student Skills"
    },
    "projects": [
      {
        "id": "project_id",
        "title": "Project Title",
        "skills": "Required Skills"
      }
    ]
  }
  ```
- **Response**:
  ```json
  {
    "matches": [
      {
        "project_id": "project_id",
        "title": "Project Title",
        "skills": "Required Skills",
        "similarity_score": 0.75
      }
    ],
    "total_projects": 1
  }
  ```

## How It Works

1. The API uses TF-IDF (Term Frequency-Inverse Document Frequency) to convert text descriptions of projects and student skills into numerical vectors.
2. Cosine similarity is calculated between the vectors to determine how well a student matches a project or vice versa.
3. The top N matches are returned, sorted by similarity score. 

## License
MIT
