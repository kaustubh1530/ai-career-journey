from openai import OpenAI

client = OpenAI()

def test_prompt(system_role, user_prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_role},
            {"role": "user", "content": user_prompt}
        ]
    )

    print("\n============================")
    print("SYSTEM:", system_role)
    print("USER:", user_prompt)
    print("\nAI RESPONSE:\n")
    print(response.choices[0].message.content)
    print("============================\n")


# 🔹 Same user prompt
user_prompt = "Summarize AI in 2 lines"

# 🔹 Different system roles
test_prompt("You are a friendly teacher", user_prompt)

test_prompt("You are a strict professor", user_prompt)

test_prompt("You are a recruiter reviewing candidates", user_prompt)

test_prompt("You are a very strict recruiter who gives harsh feedback", user_prompt)