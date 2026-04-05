def calculator_tool(expression):
    try:
        result = eval(expression)
        return f"Calculation Result: {result}"
    except:
        return "Invalid calculation input."


def summary_tool(text):
    sentences = text.split(".")
    short_summary = ".".join(sentences[:2]).strip()
    return f"Summary: {short_summary}"


def keyword_extractor_tool(text):
    keywords = []
    important_words = ["python", "fastapi", "api", "llm", "rag", "agent", "sql", "backend"]

    words = text.lower().split()
    for word in words:
        clean_word = word.strip(".,!?()")
        if clean_word in important_words and clean_word not in keywords:
            keywords.append(clean_word)

    if keywords:
        return f"Extracted Keywords: {', '.join(keywords)}"
    else:
        return "No important keywords found."


def decide_tool(user_input):
    user_input_lower = user_input.lower()

    if "calculate" in user_input_lower:
        return "calculator"
    elif "summarize" in user_input_lower:
        return "summary"
    elif "extract" in user_input_lower or "skills" in user_input_lower:
        return "keywords"
    else:
        return "unknown"


def run_agent():
    print("=== Tool Calling Career Assistant ===")
    user_input = input("What would you like help with? ")

    chosen_tool = decide_tool(user_input)

    print(f"\n[Agent Thinking] I should use: {chosen_tool}")

    if chosen_tool == "calculator":
        expression = user_input.lower().replace("calculate", "").strip()
        result = calculator_tool(expression)
        print("[Agent Action] Running calculator tool...")
        print(result)

    elif chosen_tool == "summary":
        text = user_input.lower().replace("summarize", "").strip()
        result = summary_tool(text)
        print("[Agent Action] Running summary tool...")
        print(result)

    elif chosen_tool == "keywords":
        text = user_input.lower().replace("extract", "").replace("skills", "").strip()
        result = keyword_extractor_tool(text)
        print("[Agent Action] Running keyword extraction tool...")
        print(result)

    else:
        print("[Agent Response] Sorry, I don’t know which tool to use.")


if __name__ == "__main__":
    run_agent()