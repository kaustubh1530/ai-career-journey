jobs = [
    "Python Backend Intern - Python, FastAPI, REST APIs",
    "Frontend Developer Intern - React, JavaScript, CSS",
    "AI Engineering Intern - Python, Machine Learning, OpenAI APIs",
    "Data Analyst Intern - SQL, Python, Data Analysis"
]

query = "Python AI"

keywords = query.lower().split()

print(keywords)

relevant_jobs = []

for job in jobs:
    job_lower = job.lower()

    print(f"\nChecking: {job}")

    matches = [keyword for keyword in keywords if keyword in job_lower]

    print(f"Matches: {matches}")

    if matches:
        relevant_jobs.append({
            "job": job,
            "score": len(matches)
        })

relevant_jobs.sort(
    key=lambda item: item["score"],
    reverse=True
)

print("\nRelevant Jobs:")

for item in relevant_jobs:
    print(f"- {item['job']} (Score: {item['score']})")