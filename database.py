from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class ResumeAnalysis(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    filename = db.Column(db.String(200))

    job_role = db.Column(db.String(100))

    ats_score = db.Column(db.Integer)

    skills_found = db.Column(db.Text)

    missing_skills = db.Column(db.Text)


class Job(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(200))

    company = db.Column(db.String(200))

    location = db.Column(db.String(100))

    salary = db.Column(db.String(100))

    experience = db.Column(db.String(100))

    education = db.Column(db.String(200))

    skills = db.Column(db.Text)

    description = db.Column(db.Text)

    requirements = db.Column(db.Text)