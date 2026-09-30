documents = [
    {
        "title": "Python Backend Intern",
        "text": "Python, FastAPI, REST APIs"
    },
    {
        "title": "AI Engineering Intern",
        "text": "Python, Machine Learning, OpenAI APIs"
    },
    {
        "title": "Frontend Developer Intern",
        "text": "React, JavaScript, CSS"
    },
    {
        "title": "Data Analyst Intern",
        "text": "SQL, Excel, Data Analysis"
    }
]


def keyword_score(query, document):
    query_words = set(query.lower().split())
    document_words = set(document["text"].lower().split())

    return len(query_words & document_words)


query = "Python machine learning internship"

ranked = []

for document in documents:
    score = keyword_score(query, document)

    ranked.append({
        "title": document["title"],
        "score": score
    })

ranked.sort(key=lambda x: x["score"], reverse=True)

print("\n--- Reranked Results ---")

for result in ranked:
    print(f"{result['score']} -> {result['title']}")