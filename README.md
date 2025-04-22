# Job-Project Recommendation System

A Flask-based recommendation system that matches students with relevant projects based on their skills and job profiles.

## Features
- Recommends projects to students based on their job title, skills, and interests
- Searches for students based on job title and skills
- Uses TF-IDF vectorization and cosine similarity for recommendations

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/mansour3432/Recommendation-System.git
   cd Recommendation-System
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Place your datasets in the Dataset/ directory:
   - dice_com-job_us_sample.csv
   - Final_Upwork_Dataset.csv

## Usage

1. Run the Flask application:
   ```bash
   python app.py
   ```

2. API Endpoints:
   - **Recommend projects**:
     ```bash
     POST /recommend_projects
     {
       "job_title": "Software Engineer",
       "skills": "Python, Flask, Machine Learning",
       "interests": "Web Development, AI",
       "top_n": 5
     }
     ```
   
   - **Search students**:
     ```bash
     GET /search_students?job_title=engineer&skill=python&top_n=3
     ```

## Project Structure
- `app.py`: Main application file
- `Dataset/`: Directory containing input datasets
- `requirements.txt`: Python dependencies

## License
MIT
