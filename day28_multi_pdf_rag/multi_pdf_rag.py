from openai import OpenAI
from dotenv import load_dotenv
from pypdf import PdfReader
import os
import faiss
import numpy as np

# ================================
# 1. Load API key
# ================================
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# ================================
# 2. Define folders
# ================================
documents_folder = "documents"
extracted_folder = "extracted_texts"

# ================================
# 3. Extract text from all PDFs
# ================================
all_text = ""
document_names = []

print("📂 Reading PDF files...\n")

for filename in os.listdir(documents_folder):
    if filename.endswith(".pdf"):
        pdf_path = os.path.join(documents_folder, filename)
        reader = PdfReader(pdf_path)

        pdf_text = ""
        for page in reader.pages:
            text = page.extract_text()
            if text:
                pdf_text += text + "\n"

        # Save extracted text per file
        txt_filename = filename.replace(".pdf", ".txt")
        txt_path = os.path.join(extracted_folder, txt_filename)

        with open(txt_path, "w", encoding="utf-8") as f:
            f.write(pdf_text)

        print(f"✅ Extracted: {filename}")
        document_names.append(filename)

        # Add separator so we know where each doc starts
        all_text += f"\n\n===== DOCUMENT: {filename} =====\n\n"
        all_text += pdf_text

print("\n📄 All PDFs processed successfully!")
print(f"📚 Total documents loaded: {len(document_names)}")

# ================================
# 4. Chunking function
# ================================
def chunk_text(text, chunk_size=500):
    chunks = []
    for i in range(0, len(text), chunk_size):
        chunk = text[i:i + chunk_size]
        chunks.append(chunk)
    return chunks

chunks = chunk_text(all_text, chunk_size=500)

print(f"✅ Total chunks created: {len(chunks)}")

# ================================
# 5. Generate embeddings for chunks
# ================================
response = client.embeddings.create(
    model="text-embedding-3-small",
    input=chunks
)

chunk_embeddings = [item.embedding for item in response.data]
embedding_matrix = np.array(chunk_embeddings).astype("float32")

print(f"🔢 Embedding matrix shape: {embedding_matrix.shape}")

# ================================
# 6. Store embeddings in FAISS
# ================================
dimension = embedding_matrix.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embedding_matrix)

print("📦 All document chunks stored in FAISS successfully!")

# ================================
# 7. Ask user question
# ================================
query = input("\n❓ Ask a career-related question: ")

# ================================
# 8. Embed user question
# ================================
query_response = client.embeddings.create(
    model="text-embedding-3-small",
    input=[query]
)

query_embedding = np.array([query_response.data[0].embedding]).astype("float32")

# ================================
# 9. Search top relevant chunks
# ================================
k = min(4, len(chunks))
distances, indices = index.search(query_embedding, k)

print("\n🔍 Top matching chunks:\n")

retrieved_chunks = []

for rank, idx in enumerate(indices[0]):
    if idx == -1:
        continue

    print(f"--- Match {rank+1} (Chunk #{idx}) ---")
    print(f"Distance Score: {distances[0][rank]:.4f}")
    print(chunks[idx][:500])
    print("\n")

    retrieved_chunks.append(chunks[idx])

# ================================
# 10. Combine retrieved chunks into context
# ================================
context = "\n\n".join(retrieved_chunks)

# ================================
# 11. Send context + question to OpenAI
# ================================
chat_response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {
            "role": "system",
            "content": """
You are a helpful AI career assistant.

Answer only using the provided context from the candidate's resume and job description PDFs.

Your job is to help with:
- resume-job matching
- skill comparison
- identifying missing keywords
- summarizing qualifications
- suggesting what the candidate should improve

If the answer is not clearly in the context, say:
'I could not find that information clearly in the provided documents.'
"""
        },
        {
            "role": "user",
            "content": f"""
Use the context below to answer the question.

Context:
{context}

Question:
{query}

Answer clearly, professionally, and in a helpful way.
"""
        }
    ]
)

# ================================
# 12. Print final AI answer
# ================================
final_answer = chat_response.choices[0].message.content

print("\n🤖 Final AI Career Answer:\n")
print(final_answer)