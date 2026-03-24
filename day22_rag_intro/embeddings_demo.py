from openai import OpenAI
import os
from dotenv import load_dotenv

# Load API key
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Sentences
sentences = [
    "I want a job in AI",
    "Machine learning engineer roles are growing",
    "I love playing football"
    "Data science is interesting"
    "I enjoy cooking food"
]

# Generate embeddings
response = client.embeddings.create(
    model="text-embedding-3-small",
    input=sentences
)

# Print embeddings
for i, emb in enumerate(response.data):
    print(f"\nSentence: {sentences[i]}")
    print(f"Embedding length: {len(emb.embedding)}")
    print(f"First 5 values: {emb.embedding[:5]}")