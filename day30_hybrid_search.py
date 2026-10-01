documents = [
    "AI Engineering Intern requires Python and machine learning.",
    "Frontend Developer Intern requires React and JavaScript.",
    "Data Analyst Intern requires SQL and Excel.",
    "Python Backend Intern requires Python and FastAPI."
]

query = "Python machine learning internship"

query_words = set(query.lower().split())

results = []

for doc in documents:
    doc_words = set(doc.lower().split())

    keyword_score = len(query_words & doc_words)

    results.append({
        "document": doc,
        "keyword_score": keyword_score
    })

results.sort(key=lambda x: x["keyword_score"], reverse=True)

print("\n--- Keyword Ranking ---")

for result in results:
    print(
        f"{result['keyword_score']} -> "
        f"{result['document']}"
    )