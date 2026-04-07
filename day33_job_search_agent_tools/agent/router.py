from tools.job_tools import search_jobs, summarize_job, extract_skills


def handle_user_query(user_input):
    print("\n[Agent Thought] The user wants help finding jobs and understanding them.")
    print("[Agent Action] Using job search, summarization, and skill extraction tools...\n")

    jobs = search_jobs(user_input)

    if jobs:
        print("[Agent Observation] Matching jobs found:\n")

        for job in jobs:
            summary = summarize_job(job)
            skills = extract_skills(job)

            print(f"Job Summary: {summary}")
            print(f"Required Skills: {', '.join(skills)}")
            print("-" * 50)

        print("\n[Final Answer]")
        print("These roles match your query. Focus on the listed skills to improve your chances.")
    else:
        print("[Agent Observation] No matching jobs found.")
        print("\n[Final Answer]")
        print("Sorry, I could not find relevant internship roles for that search.")