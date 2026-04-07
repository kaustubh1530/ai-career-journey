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
        description = job["description"].lower()

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