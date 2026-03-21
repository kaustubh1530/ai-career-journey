from openai import OpenAI

client = OpenAI()

def generate_text(prompt, temperature):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        temperature=temperature,
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content


prompt = "Write a short story about a student learning AI"

# 🔥 Different temperatures
temps = [0.2, 0.5, 0.8, 1.2]

for t in temps:
    print("\n==============================")
    print(f"Temperature: {t}\n")
    output = generate_text(prompt, t)
    print(output)
    print("==============================\n")