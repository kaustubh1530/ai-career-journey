documents = [
    {
        "title": "AI Engineering Intern",
        "text": "Python, Machine Learning, OpenAI APIs",
        "location": "Virginia",
        "type": "AI"
    },
    {
        "title": "Data Analyst Intern",
        "text": "SQL, Excel, Data Analysis",
        "location": "Maryland",
        "type": "Data"
    },
    {
        "title": "Frontend Developer Intern",
        "text": "React, JavaScript, CSS",
        "location": "Virginia",
        "type": "Frontend"
    }
]

location_filter = "Virginia"

filtered_documents = [
    doc for doc in documents
    if doc["location"] == location_filter
]

print("\n--- Filtered Documents ---")

for doc in filtered_documents:
    print(doc["title"], "->", doc["location"])