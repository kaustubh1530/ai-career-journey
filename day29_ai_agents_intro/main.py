def search_jobs():
    return [
        "Software Engineering Intern - Rockville, MD",
        "Python Developer Intern - Baltimore, MD",
        "AI Research Intern - Washington, DC"
    ]


def review_resume():
    return "Your resume should highlight Python, FastAPI, RAG, and AI projects."


def suggest_skills():
    return [
        "FastAPI",
        "OpenAI API",
        "RAG",
        "Vector Databases",
        "Agentic AI"
    ]


def agent_router(user_input):
    user_input = user_input.lower()

    if "job" in user_input or "internship" in user_input:
        print("\n[Agent Thinking] You want job-related help.")
        print("[Agent Action] Using job search tool...\n")

        jobs = search_jobs()
        print("Here are some job suggestions:")
        for job in jobs:
            print("-", job)

    elif "resume" in user_input:
        print("\n[Agent Thinking] You want resume feedback.")
        print("[Agent Action] Using resume review tool...\n")

        feedback = review_resume()
        print("Resume Feedback:")
        print(feedback)

    elif "skill" in user_input or "learn" in user_input:
        print("\n[Agent Thinking] You want learning guidance.")
        print("[Agent Action] Using skill suggestion tool...\n")

        skills = suggest_skills()
        print("Recommended skills to learn:")
        for skill in skills:
            print("-", skill)

    else:
        print("\n[Agent Thinking] I am not sure which tool to use.")
        print("[Agent Response] Please ask about jobs, resume, or skills.")


def main():
    print("=== Career AI Agent (Mock Version) ===")
    user_input = input("What do you need help with today? ")

    agent_router(user_input)


if __name__ == "__main__":
    main()