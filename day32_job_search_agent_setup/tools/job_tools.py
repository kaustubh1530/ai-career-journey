import json


def load_jobs():
    with open("data/sample_jobs.json", "r") as file:
        jobs = json.load(file)
    return jobs


def search_jobs(user_query):
    jobs = load_jobs()
    matched_jobs = []

    user_query = user_query.lower()

    for job in jobs:
        title = job["title"].lower()
        location = job["location"].lower()

        if title in user_query or location in user_query or "intern" in user_query:
            matched_jobs.append(job)

    return matched_jobs