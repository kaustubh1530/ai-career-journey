from openai import OpenAI
import faiss
import numpy as np

client = OpenAI()

documents = [
    "Python Backend Intern: Python, FastAPI, REST APIs.",
    "AI Engineering Intern: Python, Machine Learning, OpenAI APIs.",
    "Frontend Developer Intern: React, JavaScript, CSS.",
    "Data Analyst Intern: SQL, Excel, Data Analysis.",
]

response = client.embeddings.create(
    model="text-embedding-3-small",
    input=documents
)

embeddings = [item.embedding for item in response.data]

embedding_matrix = np.array(embeddings, dtype="float32")

index = faiss.IndexFlatL2(1536)
index.add(embedding_matrix)

print("Number of documents:", len(documents))
print("Number of embeddings:", len(embeddings))
print("Embedding dimensions:", len(embeddings[0]))
print("FAISS vectors stored:", index.ntotal)

query = "Which internship uses React?"

query_response = client.embeddings.create(
    model="text-embedding-3-small",
    input=query
)

query_embedding = np.array(
    [query_response.data[0].embedding],
    dtype="float32"
)

print("Query embedding shape:", query_embedding.shape)

distances, indices = index.search(query_embedding, 2)

print("Distances:", distances)
print("Indices:", indices)

retrieved_documents = [
    documents[i]
    for i in indices[0]
]

context = "\n".join(retrieved_documents)

print("\nRetrieved Context:")
print(context)

prompt = f"""
Answer the user's question using only the provided context.

Context:
{context}

Question:
{query}
"""

print("\nPrompt:")
print(prompt)

response = client.responses.create(
    model="gpt-5-mini",
    input=prompt
)

answer = response.output_text

print("\nFinal Answer:")
print(answer)