def search_jobs_tool():
    return [
        "Software Engineering Intern - Bethesda, MD",
        "Backend Developer Intern - Arlington, VA",
        "AI Engineering Intern - Washington, DC"
    ]


def recommend_skills_tool():
    return ["Python", "FastAPI", "RAG", "APIs", "Agentic AI"]


def review_resume_tool():
    return "Your resume should highlight projects, GitHub links, and technical skills more clearly."


def react_agent(user_input):
    user_input = user_input.lower()

    print("\n=== ReAct Agent Execution ===")

    # THOUGHT
    if "job" in user_input or "internship" in user_input:
        print("\n[Thought] The user is asking about jobs or internships.")
        print("[Action] Use search_jobs_tool()")

        # ACTION
        jobs = search_jobs_tool()

        # OBSERVATION
        print("[Observation] Found internship opportunities:")
        for job in jobs:
            print("-", job)

        # FINAL ANSWER
        print("\n[Final Answer]")
        print("Here are some internship roles you can explore above.")

    elif "skill" in user_input or "learn" in user_input:
        print("\n[Thought] The user wants guidance on what skills to learn.")
        print("[Action] Use recommend_skills_tool()")

        # ACTION
        skills = recommend_skills_tool()

        # OBSERVATION
        print("[Observation] Recommended technical skills:")
        for skill in skills:
            print("-", skill)

        # FINAL ANSWER
        print("\n[Final Answer]")
        print("You should focus first on Python, FastAPI, and RAG for strong AI/backend preparation.")

    elif "resume" in user_input:
        print("\n[Thought] The user wants resume feedback.")
        print("[Action] Use review_resume_tool()")

        # ACTION
        feedback = review_resume_tool()

        # OBSERVATION
        print("[Observation] Resume review completed:")
        print(feedback)

        # FINAL ANSWER
        print("\n[Final Answer]")
        print("Improve your resume by emphasizing technical projects and relevant skills.")

    else:
        print("\n[Thought] I cannot clearly determine the user's goal.")
        print("[Action] No suitable tool found.")
        print("[Observation] Missing task clarity.")
        print("\n[Final Answer]")
        print("Please ask about jobs, resume feedback, or skills to learn.")


def main():
    print("=== ReAct Career Agent ===")
    user_input = input("What would you like help with today? ")
    react_agent(user_input)


if __name__ == "__main__":
    main()