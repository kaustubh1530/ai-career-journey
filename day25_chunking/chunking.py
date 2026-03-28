# ================================
# DAY 25 — CHUNKING TEXT FOR RAG
# ================================

# 1. Read extracted text file
with open("extracted_text.txt", "r", encoding="utf-8") as file:
    full_text = file.read()

print("📄 Full text loaded successfully!")
print(f"📝 Total characters: {len(full_text)}")

# ================================
# 2. Chunking function
# ================================
def chunk_text(text, chunk_size=500):
    chunks = []
    
    for i in range(0, len(text), chunk_size):
        chunk = text[i:i + chunk_size]
        chunks.append(chunk)
    
    return chunks

# ================================
# 3. Split text into chunks
# ================================
chunks = chunk_text(full_text, chunk_size=500)

print(f"\n✅ Total chunks created: {len(chunks)}")

# ================================
# 4. Preview chunks
# ================================
for i, chunk in enumerate(chunks):
    print(f"\n--- Chunk {i+1} ---")
    print(chunk[:300])   # Show first 300 characters of each chunk

# ================================
# 5. Save chunks to file
# ================================
with open("chunks_output.txt", "w", encoding="utf-8") as file:
    for i, chunk in enumerate(chunks):
        file.write(f"--- Chunk {i+1} ---\n")
        file.write(chunk + "\n\n")

print("\n💾 Chunks saved to chunks_output.txt")