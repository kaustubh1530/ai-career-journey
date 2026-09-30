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

# Create document embeddings
response = client.embeddings.create(
    model="text-embedding-3-small",
    input=documents
)

embeddings = [item.embedding for item in response.data]

# Build FAISS index
embedding_matrix = np.array(embeddings, dtype="float32")

index = faiss.IndexFlatL2(len(embeddings[0]))
index.add(embedding_matrix)


test_cases = [
    {
        "query": "Which internship requires machine learning?",
        "expected": "AI Engineering Intern",
    },
    {
        "query": "Which internship uses React?",
        "expected": "Frontend Developer Intern",
    },
    {
        "query": "Which internship requires SQL?",
        "expected": "Data Analyst Intern",
    },
]


def retrieve(query, k=2):
    query_response = client.embeddings.create(
        model="text-embedding-3-small",
        input=query
    )

    query_embedding = np.array(
        [query_response.data[0].embedding],
        dtype="float32"
    )

    distances, indices = index.search(query_embedding, k)

    return [documents[i] for i in indices[0]]


hits_at_1 = 0
hits_at_2 = 0

for test in test_cases:
    results = retrieve(test["query"], k=2)

    hit1 = any(test["expected"] in result for result in results[:1])
    hit2 = any(test["expected"] in result for result in results[:2])

    hits_at_1 += hit1
    hits_at_2 += hit2

    print(f"\nQuestion: {test['query']}")
    print(f"Expected: {test['expected']}")
    print("Results:")

    for result in results:
        print("-", result)

    print("Hit@1:", hit1)
    print("Hit@2:", hit2)


total = len(test_cases)

print("\n--- Retrieval Evaluation ---")
print(f"Hit@1: {hits_at_1}/{total} = {hits_at_1 / total:.2f}")
print(f"Hit@2: {hits_at_2}/{total} = {hits_at_2 / total:.2f}")