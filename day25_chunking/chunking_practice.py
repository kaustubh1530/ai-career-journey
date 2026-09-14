text = """
Python is a programming language.
Python is widely used in artificial intelligence.
Machine learning uses data to learn patterns.
RAG systems retrieve relevant information.
Embeddings convert text into vectors.
FAISS searches vectors efficiently.
"""

# Convert text into a list of words
words = text.split()

print("Total words:", len(words))
print("\nWords:", words)

sentences = [
    sentence.strip()
    for sentence in text.strip().split(".")
    if sentence.strip()
]

print("\nSentences:")

for sentence in sentences:
    print("-", sentence)

chunk_size = 15

chunks = []
current_chunk = []
current_word_count = 0

for sentence in sentences:

    sentence_word_count = len(sentence.split())

    if current_word_count + sentence_word_count <= chunk_size:
        current_chunk.append(sentence)
        current_word_count += sentence_word_count

    else:
        chunks.append(" ".join(current_chunk))

        current_chunk = [sentence]
        current_word_count = sentence_word_count

# Add the final chunk
if current_chunk:
    chunks.append(" ".join(current_chunk))

print("\nSentence-Aware Chunks:")

for i, chunk in enumerate(chunks):
    print(f"\nChunk {i + 1}:")
    print(chunk)
    print("Word count:", len(chunk.split()))

chunk_data = []

for i, chunk in enumerate(chunks):
    chunk_data.append({
        "chunk_id": i + 1,
        "text": chunk,
        "source": "practice_document.txt"
    })

print("\nChunk Data:")

for item in chunk_data:
    print(item)