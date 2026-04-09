import json


def load_jobs():
    with open("data/sample_jobs.json", "r") as file:
        return json.load(file)


def search_jobs(user_query):
    jobs = load_jobs()
    matched_jobs = []
    query = user_query.lower()

    for job in jobs:
        title = job["title"].lower()
        location = job["location"].lower()

        if (
            "intern" in query
            or title in query
            or location in query
            or "ai" in query and "ai" in title
            or "backend" in query and "backend" in title
            or "software" in query and "software" in title
        ):
            matched_jobs.append(job)

    return matched_jobs


def summarize_job(job):
    return f"{job['title']} at {job['company']} in {job['location']}: {job['description']}"


def extract_skills(job):
    return job["skills"]


def calculate_match(user_skills, job_skills):
    user_skills_lower = [skill.lower().strip() for skill in user_skills]
    job_skills_lower = [skill.lower().strip() for skill in job_skills]

    matched = [skill for skill in job_skills_lower if skill in user_skills_lower]
    missing = [skill for skill in job_skills_lower if skill not in user_skills_lower]

    match_score = int((len(matched) / len(job_skills_lower)) * 100)

    return match_score, matched, missing