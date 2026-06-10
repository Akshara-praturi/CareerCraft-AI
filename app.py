from flask import Flask, request, jsonify
from flask_cors import CORS
import os

from analyzer import extract_text_from_pdf, analyze_resume

from database import db, ResumeAnalysis, Job

app = Flask(__name__)

CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///careercraft.db"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

UPLOAD_FOLDER = "uploads"

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


@app.route("/")
def home():
    return "Resume Analyzer Backend Running"


@app.route("/analyze", methods=["POST"])
def analyze():

    if "resume" not in request.files:
        return jsonify({"error": "No file uploaded"})

    file = request.files["resume"]

    filepath = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    file.save(filepath)

    text = extract_text_from_pdf(filepath)

    job_role = request.form["job_role"]

    result = analyze_resume(text, job_role)

    new_analysis = ResumeAnalysis(

        filename=file.filename,

        job_role=job_role,

        ats_score=result["ats_score"],

        skills_found=", ".join(
            result["skills_found"]
        ),

        missing_skills=", ".join(
            result["missing_skills"]
        )
    )

    db.session.add(new_analysis)

    db.session.commit()

    return jsonify(result)


@app.route("/jobs", methods=["GET"])
def get_jobs():

    jobs = Job.query.all()

    jobs_list = []

    for job in jobs:

        jobs_list.append({

            "id": job.id,

            "title": job.title,

            "company": job.company,

            "location": job.location,

            "salary": job.salary,

            "experience": job.experience,

            "education": job.education,

            "skills": job.skills,

            "description": job.description,

            "requirements": job.requirements
        })

    return jsonify(jobs_list)


if __name__ == "__main__":

    with app.app_context():
        db.create_all()

    app.run(debug=True)