from tools.job_tools import search_jobs


def handle_user_query(user_input):
    print("\n[Agent Thought] The user wants job-related help.")
    print("[Agent Action] Using search_jobs tool...\n")

    jobs = search_jobs(user_input)

    if jobs:
        print("[Agent Observation] Matching jobs found:\n")
        for job in jobs:
            print(f"Title: {job['title']}")
            print(f"Company: {job['company']}")
            print(f"Location: {job['location']}")
            print(f"Skills: {', '.join(job['skills'])}")
            print("-" * 40)

        print("\n[Final Answer]")
        print("These are some matching internship opportunities based on your search.")
    else:
        print("[Agent Observation] No matching jobs found.")
        print("\n[Final Answer]")
        print("Sorry, I could not find relevant jobs for that query.")