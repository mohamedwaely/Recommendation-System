from flask import Flask, request, jsonify
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

app = Flask(__name__)

# Load and preprocess datasets
students_df = pd.read_csv("Dataset/dice_com-job_us_sample.csv")[["jobtitle", "jobdescription", "skills"]]
projects_df = pd.read_csv("Dataset/Final_Upwork_Dataset.csv")
projects_df = projects_df[['Job Title', 'Description', 'Category_1', 'Category_2', 'Category_3',
                          'Category_4', 'Category_5', 'Category_6', 'Category_7', 'Category_8',
                          'Category_9']]

students_df = students_df.copy().fillna("")
projects_df = projects_df.copy().fillna("")

students_df["student_profile"] = (
    students_df["jobtitle"] + " " + students_df["jobdescription"] + " " + students_df["skills"]
)

projects_df["project_requirements"] = (
    projects_df["Category_1"].astype(str) + " " + projects_df["Category_2"].astype(str) + " " +
    projects_df["Category_3"].astype(str) + " " + projects_df["Category_4"].astype(str) + " " +
    projects_df["Category_5"].astype(str) + " " + projects_df["Category_6"].astype(str) + " " +
    projects_df["Category_7"].astype(str) + " " + projects_df["Category_8"].astype(str) + " " +
    projects_df["Category_9"].astype(str)
)

projects_df = projects_df[['Job Title', 'Description', 'project_requirements']]

# Build TF-IDF matrix
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(projects_df["project_requirements"])

@app.route("/recommend_projects", methods=["POST"])
def recommend_projects():
    data = request.json
    job_title = data.get("job_title", "")
    skills = data.get("skills", "")
    interests = data.get("interests", "")
    top_n = int(data.get("top_n", 5))

    student_profile = f"{job_title} {skills} {interests}"
    student_vector = vectorizer.transform([student_profile])
    cosine_similarities = linear_kernel(student_vector, tfidf_matrix).flatten()
    top_indices = cosine_similarities.argsort()[::-1][:top_n]
    
    recommended = projects_df.iloc[top_indices][["Job Title", "Description"]].to_dict(orient="records")
    return jsonify(recommended)

@app.route("/search_students", methods=["GET"])
def search_students():
    job_title = request.args.get("job_title", "").lower()
    skill = request.args.get("skill", "").lower()
    top_n = int(request.args.get("top_n", 5))

    results = students_df.copy()
    if job_title:
        results = results[results["jobtitle"].str.lower().str.contains(job_title)]
    if skill:
        results = results[results["skills"].str.lower().str.contains(skill)]

    results = results.head(top_n)[["jobtitle", "skills", "student_profile"]]
    return jsonify(results.to_dict(orient="records"))

if __name__ == "__main__":
    app.run(debug=True)
