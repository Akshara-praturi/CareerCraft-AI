import PyPDF2

job_roles = {

    "Frontend Developer": [
        "react",
        "html",
        "css",
        "javascript"
    ],

    "Python Developer": [
        "python",
        "flask",
        "sql",
        "api"
    ],

    "Data Analyst": [
        "python",
        "sql",
        "excel",
        "power bi",
        "pandas"
    ],

    "Full Stack Developer": [
        "html",
        "css",
        "javascript",
        "react",
        "node",
        "express",
        "mysql",
        "git",
        "rest",
        "api"
    ]
}


def extract_text_from_pdf(pdf_path):

    text = ""

    with open(pdf_path, "rb") as file:

        reader = PyPDF2.PdfReader(file)

        for page in reader.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text

    return text.lower()


def analyze_resume(text, job_role):

    text = text.lower()

    required_skills = job_roles.get(job_role, [])

    found_skills = []

    for skill in required_skills:

        if skill.lower() in text:
            found_skills.append(skill)

    total_skills = len(required_skills)

    ats_score = (
        int((len(found_skills) / total_skills) * 100)
        if total_skills > 0
        else 0
    )

    missing_skills = [
        skill
        for skill in required_skills
        if skill not in found_skills
    ]

    suggestions = []

    if ats_score < 50:

        suggestions.append(
            "Add more relevant technical skills."
        )

        suggestions.append(
            "Include projects matching the job role."
        )

    elif ats_score < 70:

        suggestions.append(
            "Improve project descriptions with measurable outcomes."
        )

        suggestions.append(
            "Add more industry-relevant keywords."
        )

    else:

        suggestions.append(
            "Excellent match for the selected role."
        )

        suggestions.append(
            "Keep your resume updated with recent projects."
        )

    return {
        "ats_score": ats_score,
        "skills_found": found_skills,
        "missing_skills": missing_skills,
        "suggestions": suggestions
    }