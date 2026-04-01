from openai import OpenAI
from dotenv import load_dotenv
import os
import faiss
import numpy as np

# 1. Load API key

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 2. Load extracted text

with open("extracted_text.txt", "r", encoding="utf-8") as file:
    full_text = file.read()

print("📄 Text loaded successfully!")
print(f"📝 Total characters: {len(full_text)}")

# 3. Chunking function

def chunk_text(text, chunk_size=500):
    chunks = []
    for i in range(0, len(text), chunk_size):
        chunk = text[i:i + chunk_size]
        chunks.append(chunk)
    return chunks

chunks = chunk_text(full_text, chunk_size=500)
print(f"✅ Total chunks created: {len(chunks)}")

# 4. Generate embeddings for chunks

response = client.embeddings.create(
    model="text-embedding-3-small",
    input=chunks
)

chunk_embeddings = [item.embedding for item in response.data]
embedding_matrix = np.array(chunk_embeddings).astype("float32")

print(f"🔢 Embedding matrix shape: {embedding_matrix.shape}")

# 5. Store embeddings in FAISS

dimension = embedding_matrix.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embedding_matrix)

print("📦 Chunks stored in FAISS successfully!")

# 6. Ask user question

query = input("\n❓ Ask a question about the document: ")

# 7. Embed the user question

query_response = client.embeddings.create(
    model="text-embedding-3-small",
    input=[query]
)

query_embedding = np.array([query_response.data[0].embedding]).astype("float32")

# 8. Search top relevant chunks

k = min(3, len(chunks))
distances, indices = index.search(query_embedding, k)

print("\n🔍 Top matching chunks:\n")

retrieved_chunks = []

for rank, idx in enumerate(indices[0]):
    if idx == -1:
        continue

    print(f"--- Match {rank+1} (Chunk #{idx}) ---")
    print(f"Distance Score: {distances[0][rank]:.4f}")
    print(chunks[idx][:400])
    print("\n")

    retrieved_chunks.append(chunks[idx])

# 9. Combine retrieved chunks into context

context = "\n\n".join(retrieved_chunks)

# 10. Send context + question to OpenAI

chat_response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {
            "role": "system",
            "content": "You are a helpful AI assistant. Answer only based on the provided context. If the answer is not in the context, say: 'I could not find that information in the document.'"
        },
        {
            "role": "user",
            "content": f"""
Use the context below to answer the question.

Context:
{context}

Question:
{query}

Answer clearly and professionally.
"""
        }
    ]
)

# 11. Print final AI answer

final_answer = chat_response.choices[0].message.content

print("\n🤖 Final AI Answer:\n")
print(final_answer)

#“I built a Retrieval-Augmented Generation system using OpenAI embeddings, FAISS vector search, and grounded answer generation.”