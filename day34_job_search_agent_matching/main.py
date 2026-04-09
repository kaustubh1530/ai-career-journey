from agent.router import handle_user_query


def main():
    print("=== InternMatch AI ===")
    user_query = input("What type of internship/job are you looking for? ")
    user_skills_input = input("Enter your current skills (comma-separated): ")

    user_skills = [skill.strip() for skill in user_skills_input.split(",")]

    handle_user_query(user_query, user_skills)


if __name__ == "__main__":
    main()