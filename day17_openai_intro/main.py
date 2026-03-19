from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": "Write a professional email asking for internship"}
    ]
)

print(response.choices[0].message.content)