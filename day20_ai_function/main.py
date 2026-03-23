from openai import OpenAI

client = OpenAI()

# 🔥 Reusable AI Function
def generate_text(prompt, temperature=0.7):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        temperature=temperature,
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": prompt}
        ]
    )
    
    return response.choices[0].message.content


# 🧪 Test the function

print(generate_text("Write a cover letter for a data analyst internship"))