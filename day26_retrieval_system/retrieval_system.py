from openai import OpenAI
from dotenv import load_dotenv
import os
import faiss
import numpy as np

# ================================
# 1. Load API key
# ================================
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# ================================
# 2. Load extracted text
# ================================
with open("extracted_text.txt", "r", encoding="utf-8") as file:
    full_text = file.read()

print("📄 Text loaded successfully!")
print(f"📝 Total characters: {len(full_text)}")

# ================================
# 3. Chunking function
# ================================
def chunk_text(text, chunk_size=700):
    paragraphs = text.split("\n\n")
    chunks = []
    current_chunk = ""

    for para in paragraphs:
        para = para.strip()

        if not para:
            continue  # skip empty paragraphs

        if len(current_chunk) + len(para) < chunk_size:
            current_chunk += para + "\n\n"
        else:
            if current_chunk.strip():
                chunks.append(current_chunk.strip())
            current_chunk = para + "\n\n"

    if current_chunk.strip():
        chunks.append(current_chunk.strip())

    return chunks

chunks = chunk_text(full_text, chunk_size=500)
print(f"✅ Total chunks created: {len(chunks)}")

# ================================
# 4. Generate embeddings for chunks
# ================================
response = client.embeddings.create(
    model="text-embedding-3-small",
    input=chunks
)

chunk_embeddings = [item.embedding for item in response.data]

# Convert to NumPy array
embedding_matrix = np.array(chunk_embeddings).astype("float32")

print(f"🔢 Embedding matrix shape: {embedding_matrix.shape}")

# ================================
# 5. Store in FAISS
# ================================
dimension = embedding_matrix.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embedding_matrix)

print("📦 Chunks stored in FAISS successfully!")

# ================================
# 6. Ask a question
# ================================
query = input("\n❓ Ask a question about the document: ")

query_response = client.embeddings.create(
    model="text-embedding-3-small",
    input=[query]
)

query_embedding = np.array([query_response.data[0].embedding]).astype("float32")

# ================================
# 7. Search top 3 relevant chunks
# ================================
k = min(3, len(chunks))
distances, indices = index.search(query_embedding, k)

print("\n🔍 Top matching chunks:\n")

for rank, idx in enumerate(indices[0]):
    if idx == -1:
        continue   # skip invalid FAISS placeholder results

    print(f"--- Match {rank+1} (Chunk #{idx}) ---")
    print(f"Distance Score: {distances[0][rank]:.4f}")
    print(chunks[idx][:400])
    print("\n")