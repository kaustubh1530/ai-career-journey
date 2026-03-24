from openai import OpenAI
import os
from dotenv import load_dotenv
import faiss
import numpy as np

# ================================
# 1. Load API Key
# ================================
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# ================================
# 2. Our Knowledge Base (Data)
# ================================
documents = [
    "I want a job in AI",
    "Machine learning engineers build models",
    "Data science is a growing field",
    "Football is a popular sport",
    "Cooking is a useful life skill",
    "I am a batting allrounder",
    "My Idol is Virat Kohli"
]

# ================================
# 3. Convert Documents → Embeddings
# ================================
response = client.embeddings.create(
    model="text-embedding-3-small",
    input=documents
)

# Extract vectors
embeddings = [item.embedding for item in response.data]

# Convert to numpy array (FAISS requirement)
embeddings = np.array(embeddings).astype("float32")

# ================================
# 4. Create FAISS Index
# ================================
dimension = embeddings.shape[1]  # vector size (1536)

index = faiss.IndexFlatL2(dimension)

# Add embeddings to FAISS
index.add(embeddings)

print("✅ FAISS index created with", index.ntotal, "documents")

# ================================
# 5. User Query
# ================================
query = "How to get a job in artificial intelligence?"

# Convert query → embedding
query_embedding = client.embeddings.create(
    model="text-embedding-3-small",
    input=query
).data[0].embedding

query_embedding = np.array([query_embedding]).astype("float32")

# ================================
# 6. Search (CORE MAGIC)
# ================================
k = 3  # top 3 results

distances, indices = index.search(query_embedding, k)

# ================================
# 7. Show Results
# ================================
print("\n🔍 Query:", query)

print("\nTop matches:")
for i, idx in enumerate(indices[0]):
    print(f"{i+1}. {documents[idx]} (distance: {distances[0][i]})")