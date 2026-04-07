from agent.router import handle_user_query


def main():
    print("=== Job Search AI Agent v2 ===")
    user_input = input("Enter your internship/job search request: ")
    handle_user_query(user_input)


if __name__ == "__main__":
    main()