from openai import OpenAI

client = OpenAI()

# 🔥 Reusable function (from Day 20)
def generate_text(prompt, temperature=0.7):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        temperature=temperature,
        messages=[
            {"role": "system", "content": "You are a professional career coach who writes strong cover letters."},
            {"role": "user", "content": prompt}
        ]
    )
    
    return response.choices[0].message.content


# 🧠 Step 1: Take user input
job_description = input("Enter job description:\n")

# 🧠 Step 2: Create prompt
prompt = f"""
Write a professional and tailored cover letter based on the following job description.

Job Description:
{job_description}

The cover letter should:
- Be concise and professional
- Highlight relevant skills (Python, FastAPI, AI, APIs)
- Show enthusiasm for the role
- Be ready to send
"""

# 🧠 Step 3: Generate cover letter
cover_letter = generate_text(prompt, temperature=0.7)

# 🧠 Step 4: Save to file
with open("cover_letter.txt", "w") as file:
    file.write(cover_letter)

print("\n✅ Cover letter generated and saved as cover_letter.txt\n")