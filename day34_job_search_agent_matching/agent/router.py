from tools.job_tools import search_jobs, summarize_job, extract_skills, calculate_match


def handle_user_query(user_query, user_skills):
    print("\n[Agent Thought] The user wants internship recommendations based on their skills.")
    print("[Agent Action] Searching jobs and calculating skill matches...\n")

    jobs = search_jobs(user_query)

    if jobs:
        ranked_jobs = []

        for job in jobs:
            skills = extract_skills(job)
            match_score, matched, missing = calculate_match(user_skills, skills)
            ranked_jobs.append((job, match_score, matched, missing))

        ranked_jobs.sort(key=lambda x: x[1], reverse=True)

        print("[Agent Observation] Matching jobs ranked for you:\n")

        for job, score, matched, missing in ranked_jobs:
            summary = summarize_job(job)

            print(f"Job Summary: {summary}")
            print(f"Match Score: {score}%")
            print(f"Matched Skills: {', '.join(matched) if matched else 'None'}")
            print(f"Missing Skills: {', '.join(missing) if missing else 'None'}")
            print("-" * 60)

        print("\n[Final Answer]")
        print("These roles are ranked based on how well your current skills match each job.")
        print("Focus on learning the missing skills to improve your fit.")
    else:
        print("[Agent Observation] No matching jobs found.")
        print("\n[Final Answer]")
        print("Sorry, I could not find relevant internship roles for that search.")