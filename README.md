# Day 1: Python Basics and Calculator

## Project Overview 
This is my Day 1 project for my AI career journey. I am learning Python from scratch.

## What I Learned 
- Basic Python syntax 
- Variables and user input 
- Arithmetic operations ➕➖✖️➗
- Conditional statements (division by zero check) 
- Saving and running Python files 

python3 calculator.py
python3 day1_basics.py

## Day 2 – Smart Calculator 

**What I learned:**
- Python functions with `return`
- Parameters and user input
- Menu-driven program with loops
- Decision making with `if-else`
- Division by zero handling

**Project:**  
`day2_smart_calculator.py` – smart calculator that can:
- Add, Subtract, Multiply, Divide
- Show results interactively
- Exit cleanly

## Day 3 – Advanced Smart Calculator 

### What I learned
- Python dictionaries
- Cleaner menu systems
- Error handling using try/except
- More professional code structure

### Project
day3_calculator_loop.py

An improved calculator that:
- Uses a dictionary to store operations
- Handles invalid inputs safely
- Uses loops for continuous calculations

## Day 4 – NLP Smart Calculator 

### What I Learned 
- Parsing natural language commands from user input
- Using `str.lower()` to make input case-insensitive
- Exception handling with `try-except` to catch errors
- Extracting numbers with `re.findall()` (regular expressions)
- Handling invalid commands and division by zero gracefully

### Project
`day4_nlp_calculator.py` – smart NLP calculator that can:
- Add, Subtract, Multiply, Divide using text commands
- Commands like: `Add 5 and 3`, `Divide 10 by 2`, `Exit`
- Handle errors and invalid inputs smoothly

## Day 5 – Modular Calculator 

### What I Learned 
- Organizing code across multiple files (modules)
- Importing functions using `import` statements
- Cleaner, scalable project structure
- Reusing code efficiently
- Handling edge cases and errors

### Project
`day5_modular_calculator.py` – modular calculator that can:
- Add, Subtract, Multiply, Divide
- Uses a separate `operations.py` file for arithmetic functions
- Handles menu, input, and exit in the main file
- Clean, readable, and professional code

## Day 6 – GUI Calculator with Tkinter ️

### What I Learned
- Creating a graphical user interface (GUI) using Tkinter
- Using Entry widgets for input and display
- Creating Buttons and assigning commands
- Handling arithmetic operations with GUI buttons
- Handling errors like division by zero or empty input
- Organizing layout using grid system
- Making the calculator interactive and user-friendly

### Project
`day6_gui_calculator.py` – GUI calculator that can:
- Add, Subtract, Multiply, Divide
- Show input and results in a graphical window
- Use buttons for numbers and operations (+, -, *, /, =, C)
- Clear input with the **C** button
- Handle errors and invalid inputs gracefully

## Day 7 – Calculator with History 

### What I Learned 
- Reading from and writing to files (`open()`, `read()`, `write()`)  
- Logging calculation history for later reference  
- Organizing code using functions for clean, reusable logic  
- Handling `FileNotFoundError` when history file does not exist  
- Combining loops, conditional statements, and functions for a menu-driven interface  

### Project
`day7_calculator_history.py` – a calculator that:  
- Performs addition, subtraction, multiplication, and division  
- Saves every calculation to a history file (`calc_history.txt`)  
- Allows viewing past calculations anytime  
- Handles errors like division by zero gracefully  
- Provides a continuous menu interface for smooth user experience  

## Day 8 – Modular Calculator Project 

### What I Learned 
- How to organize Python projects into multiple files (modules)
- Importing functions from other Python files using `import`
- Separating program logic for better readability and maintenance
- Structuring a project like real-world Python applications

### Project Structure

day8_calculator/
│
├── main.py
├── operations.py
├── history.py
├── calc_history.txt


### File Responsibilities

**main.py**
- Controls the calculator menu
- Handles user input
- Calls functions from other modules

**operations.py**
- Contains math functions
- `add()`
- `subtract()`
- `multiply()`
- `divide()`

**history.py**
- Saves calculations to a file
- Displays previous calculations

# Day 9 – Calculator with Persistent History 📓

## Project Overview
For Day 9, we enhanced our calculator from Day 8 by adding **persistent history** using a JSON file. Every calculation is now saved in `calc_history.json`, allowing users to **view previous calculations even after closing the program**.

## What I Learned ✨
- Using Python **JSON** module for reading and writing structured data  
- Storing calculation history in a file for persistence  
- Modular programming by separating operations and history functions  
- Error handling for invalid input and division by zero  
- Keeping code organized with folders and professional structure  

## Project Files
- `main.py` – Main calculator program with menu and input handling  
- `calc_history.json` – Stores calculation history in JSON format  
- `operations.py` – Arithmetic functions (add, subtract, multiply, divide)  
- `history.py` – Functions to save and view history  

## Features
- Add, Subtract, Multiply, Divide  
- Input validation to prevent crashes on invalid input  
- Saves calculation history in `calc_history.json`  
- View past calculations with a menu option  
- Exit cleanly 

# Day 10 – API Calculator (Flask)

This project builds a simple REST API calculator using Flask.

## Features
- Addition
- Subtraction
- Multiplication
- Division
- JSON responses

## Example Requests

Add:
http://127.0.0.1:5000/add?a=5&b=3

Multiply:
http://127.0.0.1:5000/multiply?a=6&b=7

## Technologies Used
- Python
- Flask
- REST API

# Day 11 – Flask Web Calculator (HTML + UI)

## Project Overview
This project converts the Day 10 API calculator into a **real web application** using Flask and HTML.  
Users can enter numbers and perform basic arithmetic operations through a simple web interface.

The application demonstrates how a **Python backend communicates with an HTML frontend**.

## Technologies Used
- Python
- Flask
- HTML
- CSS

## Project Structure

day11_web_calculator

app.py → Flask backend logic

templates/

index.html → Web page for the calculator UI

static/

style.css → Styling for the calculator


## Features
- Addition
- Subtraction
- Multiplication
- Division
- Error handling for division by zero
- Simple and clean user interface

## How It Works
1. The user enters two numbers in the form.
2. The user selects an operation (+, -, *, /).
3. The form sends a POST request to the Flask backend.
4. Flask processes the operation.
5. The result is returned and displayed on the webpage.

# Day 12 – Interactive Web Calculator

This project is part of my **AI & Software Engineering learning journey** where I build projects daily and push them to GitHub.

In Day 12, I built a **fully interactive web calculator** with a real calculator-style user interface.

## Features

- Clickable calculator buttons
- Supports basic arithmetic operations
  - Addition (+)
  - Subtraction (-)
  - Multiplication (*)
  - Division (/)
- Clear display functionality
- Dynamic calculations using JavaScript
- Clean and responsive UI

## Technologies Used

- Python
- Flask
- HTML
- CSS
- JavaScript

## Project Structure

day12_calculator_ui/
│
├── app.py
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── README.md

## Learning Outcome

Through this project I learned:

- How Flask serves HTML templates
- How to connect HTML, CSS, and JavaScript
- DOM manipulation using JavaScript
- Creating interactive UI elements
- Structuring a full-stack web project

# Day 13 – Premium Liquor Inventory Web App

This project is a **web-based inventory management system** for tracking expensive liquor bottles.

## Features

- Dashboard displaying all products
- Add new product with category, location (Store/Warehouse), quantity
- Data stored in Excel file
- Uses Flask, HTML, Bootstrap, Pandas, Openpyxl

## Folder Structure

day13_liquor_inventory_app/
├── app.py
├── inventory.xlsx
├── templates/
│   ├── index.html
│   └── add_product.html
└── static/

## How to Run

1. Install dependencies:  
`pip3 install flask pandas openpyxl`

2. Run app:  
`python3 app.py`

3. Open in browser:  
`http://127.0.0.1:5000`

# Day 14: Premium Liquor Inventory Management Web App

## Overview
Day 14 focuses on enhancing the liquor inventory management system built in Day 13.  
The main goal of this day is to create a **professional dashboard**, and implement **Move Inventory** and **Search Inventory** features using Python Flask, HTML, and Bootstrap.

---

## Features Implemented

1. **Inventory Dashboard**
   - Displays all products from the Excel file.
   - Shows:
     - Product ID
     - Name
     - Category
     - Store Quantity
     - Warehouse Quantity
     - Last Updated Date
   - Clean table layout using **Bootstrap**.

2. **Add Product**
   - Add a new liquor product to inventory (continued from Day 13).

3. **Move Inventory**
   - Move bottles between Store and Warehouse.
   - Updates quantities in the Excel file.
   - Updates the last modified date automatically.

4. **Search Inventory**
   - Search products by name.
   - Displays Store and Warehouse quantities for searched items.

---

## Technology Stack
- **Backend:** Python Flask
- **Frontend:** HTML + Bootstrap
- **Data Storage:** Excel (.xlsx)
- **Libraries:** pandas, openpyxl


# Day 15 – Full Inventory Management System

This project is a Flask-based inventory management system designed for liquor store warehouse tracking.

The system allows warehouse managers to track products, move inventory to the store, monitor stock levels, and keep a record of all inventory activities.

## Features

Dashboard
- View all inventory items
- See warehouse and store quantities
- Dashboard statistics

Add Product
- Add new liquor products
- Choose category and location
- Automatically update inventory database

Move Inventory
- Move bottles from warehouse to store
- Record the employee who moved inventory
- Automatically update quantities

Search Inventory
- Search for products quickly by name

Activity Log
- Track every inventory action
- Record time, product, quantity, and employee

Inventory Check
- Compare physical stock with system stock
- Detect mismatches

Low Stock Alerts
- Warn when warehouse inventory is low

## Technologies Used

Python
Flask
Pandas
Excel Database
Bootstrap UI

## Project Structure

day15_inventory_system
│
app.py
inventory.xlsx
│
templates
  index.html
  add_product.html
  move_inventory.html
  search.html
  activity_log.html
  inventory_check.html
  layout.html
│
static
  style.css

## Future Improvements

- Barcode scanning for bottles
- Employee login system
- Real database (PostgreSQL or MySQL)
- API integration for store systems
 

 # Day 16 – Resume Analyzer API 🚀

## 📌 Overview
This project is a Resume Analyzer API built using FastAPI.  
It allows users to upload a PDF resume and automatically extracts:

- Candidate Name
- Skills
- Word Count

---

## 🛠️ Tech Stack
- Python
- FastAPI
- Uvicorn
- PyPDF2

---

## ⚙️ Features
- Upload resume (PDF only)
- Extract text from PDF
- Identify predefined skills
- Detect candidate name (basic logic)
- Return structured JSON response

---

## 📂 Project Structure

day16_resume_analyzer_api/
│── main.py
│── README.md

---

## 🚀 How to Run

### 1. Create Virtual Environment
python3 -m venv venv
source venv/bin/activate

### 2. Install Dependencies
pip install fastapi uvicorn PyPDF2 python-multipart

### 3. Run the Server
uvicorn main:app --reload

### 4. Open in Browser
http://127.0.0.1:8000/docs

---

## 🧪 API Endpoint

### POST /analyze-resume

Upload a PDF resume and get:

{
  "name": "John Doe",
  "skills_found": ["python", "sql"],
  "word_count": 300
}

---

## ⚠️ Limitations
- Only supports PDF files
- Name extraction is rule-based (not 100% accurate)

---

## 🔥 What I Learned
- Building APIs using FastAPI
- Handling file uploads in backend
- Parsing PDF files using PyPDF2
- Writing clean backend logic
- Error handling and validation

---


# Day 17 – OpenAI API Introduction 🤖

## 📌 Overview
This project demonstrates how to integrate the OpenAI API into a Python application.

The goal of Day 17 was to understand how to:
- Use API keys
- Make requests to an AI model
- Generate text responses using prompts

---

## 🛠️ Tech Stack
- Python
- OpenAI API

---

## ⚙️ Features
- Connect to OpenAI using API key
- Send prompts to AI model
- Receive and display AI-generated responses

---

## 📂 Project Structure

day17_openai_intro/
│── main.py
│── README.md

---

## 🚀 How to Run

### 1. Create Virtual Environment
python3 -m venv venv
source venv/bin/activate

### 2. Install Dependencies
pip install openai

### 3. Set API Key (Mac)
export OPENAI_API_KEY="your_api_key_here"

### 4. Run the Program
python3 main.py

---

## 🧪 Example Prompts Tested
- Explain Python in one sentence
- Write a professional email for internship request
- Summarize a paragraph about AI

---

## 🧠 What I Learned
- How APIs work in real-world applications
- How to use OpenAI models from Python
- Understanding prompts and responses
- Basics of AI integration in backend systems

---

# Day 18 – Prompt Engineering (System vs User Roles) 🤖

## 📌 Overview
This project focuses on understanding prompt engineering by exploring the difference between system and user roles in AI models.

The goal was to learn how to control AI behavior, tone, and response style using structured prompts.

---

## 🛠️ Tech Stack
- Python
- OpenAI API

---

## ⚙️ Features
- Send prompts to AI model
- Use system role to control AI behavior
- Use user role to define the task
- Compare different outputs for the same prompt

---

## 📂 Project Structure

day18_prompt_engineering/
│── main.py
│── README.md

---

## 🚀 How to Run

### 1. Create Virtual Environment
python3 -m venv venv
source venv/bin/activate

### 2. Install Dependencies
pip install openai

### 3. Set API Key (Mac)
export OPENAI_API_KEY="your_api_key_here"

### 4. Run the Program
python3 main.py

---

## 🧪 Example Experiment

### User Prompt:
Write a cover letter for a software engineering internship

### System Roles Tested:
- Helpful assistant
- Professional career coach
- Strict recruiter
- Short and direct assistant

---

## 🧠 Key Learning

### System Role
Defines the behavior and personality of the AI  
Example:
"You are a professional career coach"

### User Role
Defines the task or request  
Example:
"Write a cover letter for a software internship"

---

## 🔍 Observation
Same user prompt produced different outputs depending on the system role:
- Tone changed
- Length changed
- Level of detail changed

---

## 🔥 What I Learned
- How prompt design affects AI output
- Difference between system and user roles
- How to control AI responses
- Basics of prompt engineering

---

# Day 19 – Temperature & Creativity Control 🤖🔥

## 📌 Overview
This project explores how to control AI response behavior using the **temperature parameter** in the OpenAI API.

The goal was to understand how to adjust AI outputs between **deterministic (strict)** and **creative (random)** responses.

---

## 🛠️ Tech Stack
- Python
- OpenAI API

---

## ⚙️ Features
- Generate AI responses using different temperature values
- Compare outputs for the same prompt
- Understand how creativity and randomness affect results

---

## 📂 Project Structure

day19_temperature_control/
│── main.py
│── README.md

---

## 🚀 How to Run

### 1. Create Virtual Environment
python3 -m venv venv
source venv/bin/activate

### 2. Install Dependencies
pip install openai

### 3. Set API Key (Mac)
export OPENAI_API_KEY="your_api_key_here"

### 4. Run the Program
python3 main.py

---

## 🧪 Experiment

### Prompt Used:
Write a short story about a student learning AI

### Temperature Values Tested:
- 0.2 → Very structured and predictable
- 0.5 → Balanced output
- 0.8 → More expressive and creative
- 1.2 → Highly creative and varied responses

---

## 🧠 Key Learning

### What is Temperature?
Temperature controls the randomness of AI output.

- Low temperature → More consistent, factual responses
- High temperature → More creative, diverse responses

---

## 🔍 Observation
The same prompt produced different outputs based on temperature:
- Tone and style changed
- Creativity increased with higher values
- Structure became less strict at higher values

---

## 🔥 Real-World Usage

### Low Temperature (0.2–0.4)
- Resume analysis
- Data extraction
- Backend APIs
- Chatbots requiring accuracy

### High Temperature (0.7–1.2)
- Story writing
- Cover letters
- Creative content generation

---

## 🚀 What I Learned
- How to control AI creativity
- Importance of temperature in AI applications
- How to fine-tune AI responses for different use cases

---

# Day 20 – Reusable AI Function 🤖

## 📌 Overview
This project focuses on building a reusable AI function using the OpenAI API.

Instead of writing API calls repeatedly, a single function is created to generate AI responses dynamically. This introduces the concept of **code abstraction** and prepares the foundation for building scalable AI applications.

---

## 🛠️ Tech Stack
- Python
- OpenAI API

---

## ⚙️ Features
- Reusable function for AI text generation
- Supports custom prompts
- Supports temperature control for creativity
- Clean and scalable code structure

---

## 📂 Project Structure

day20_ai_function/
│── main.py
│── README.md

---

## 🚀 How to Run

### 1. Create Virtual Environment
python3 -m venv venv
source venv/bin/activate

### 2. Install Dependencies
pip install openai

### 3. Set API Key (Mac)
export OPENAI_API_KEY="your_api_key_here"

### 4. Run the Program
python3 main.py

---

## 💡 Code Example

def generate_text(prompt, temperature=0.7):
    # Sends prompt to OpenAI API
    # Returns generated response

---

## 🧪 Example Prompts Tested
- Write a professional email asking for an internship  
- Explain Python in simple terms  
- Write a short motivational quote  

---

## 🧠 Key Learning

### What is Abstraction?
Abstraction means hiding complex implementation details and exposing only the necessary functionality.

Instead of repeating API calls, a single reusable function is used.

---

## 🔥 Why This Matters
- Cleaner code  
- Easier to maintain  
- Scalable for larger projects  
- Foundation for real AI applications  

---

## 🚀 What I Learned
- How to create reusable AI functions  
- How to structure AI-based code  
- How to control responses using parameters like temperature  

---

# Day 21 – AI Cover Letter Generator 🤖📄

## 📌 Overview
This project is an AI-powered Cover Letter Generator that creates professional and tailored cover letters based on a given job description.

It uses the OpenAI API along with prompt engineering techniques to generate high-quality, job-specific cover letters automatically.

---

## 🛠️ Tech Stack
- Python
- OpenAI API

---

## ⚙️ Features
- Accepts job description as input
- Generates a professional cover letter using AI
- Uses prompt engineering for structured output
- Saves generated cover letter to a text file
- Reusable AI function for text generation

---

## 📂 Project Structure

day21_ai_cover_letter/
│── main.py
│── cover_letter.txt
│── README.md

---

## 🚀 How to Run

### 1. Create Virtual Environment
python3 -m venv venv
source venv/bin/activate

### 2. Install Dependencies
pip install openai

### 3. Set API Key (Mac)
export OPENAI_API_KEY="your_api_key_here"

### 4. Run the Program
python3 main.py

---

## 🧪 Example Input

Enter job description:

Looking for a software engineering intern with knowledge of Python, APIs, and problem solving skills.

---

## 📄 Example Output
A complete, professional cover letter tailored to the job description will be generated and saved as:

cover_letter.txt

---

## 🧠 Key Concepts

### Prompt Engineering
The AI is guided using structured instructions to:
- Maintain professionalism
- Highlight relevant skills
- Match the job requirements

---

### Reusable Function
A reusable function is used to generate AI responses:

def generate_text(prompt, temperature=0.7)

This improves code structure and scalability.

---

## 🔥 Real-World Use Case
- Automate job applications
- Generate customized cover letters quickly
- Improve productivity for job seekers

---

## 🚀 What I Learned
- Building real-world AI applications
- Using OpenAI API effectively
- Designing structured prompts
- Saving AI-generated outputs to files

---

# Day 22 — RAG & Embeddings Intro

## 🎯 Goal
Today we start **Week 5** of the AI Career Journey:
- Understand **RAG (Retrieval-Augmented Generation)**
- Understand **Embeddings**
- Generate your **first embeddings** in Python

---

## 🧠 Concepts Learned

### 1. RAG (Retrieval-Augmented Generation)
- AI answers **based on your data**, not guessing
- Workflow: `Store knowledge → Search → Provide to AI → Generate answer`

### 2. Embeddings
- Convert **text → numbers (vectors)**
- Similar meaning → similar vectors
- Key for **semantic search** and RAG systems

---

# Day 23 — Vector Search with FAISS

## 🎯 Goal
Build a basic **AI-powered search system** using:
- Embeddings
- FAISS (vector database)

---

## 🧠 Concepts Learned

### 1. Vector Search
- Instead of keyword matching, we search by **meaning**
- Example:
  - Query: "AI jobs"
  - Result: "Machine learning engineer roles"

---

### 2. Similarity Search
- Compare vectors using **distance**
- Closer vectors → more similar meaning

---

### 3. FAISS (Facebook AI Similarity Search)
- Library for **fast vector search**
- Stores embeddings and retrieves closest matches

---

### 4. NumPy Arrays
- FAISS requires embeddings in **NumPy format**
- Converted list → array using `np.array()`

---

# Day 24 — PDF Loader for RAG

## 🎯 Goal
Learn how to load and extract text from a **PDF document** in Python as the first step of a real-world **RAG pipeline**.

---

## 🧠 Concepts Learned

### 1. Document Loader
A **document loader** is code that:
- opens a file
- reads its content
- converts it into usable text for AI systems

Today’s file type:
- **PDF**

---

### 2. Why PDFs Matter in RAG
Real-world AI apps often need to answer questions from:
- resumes
- research papers
- notes
- policies
- manuals

To do that, we first need to:
1. Load the PDF
2. Extract the text
3. Prepare it for chunking and retrieval

---

### 3. Text Extraction
Using the **pypdf** library, we:
- opened a PDF file
- looped through each page
- extracted text
- saved the full extracted content into a `.txt` file

---

# Day 25 — Chunking Text for RAG

## 🎯 Goal
Learn how to split large extracted document text into **smaller chunks** so it can be used effectively in a **RAG (Retrieval-Augmented Generation)** pipeline.

---

## 🧠 Concepts Learned

### 1. What is Chunking?
Chunking means:
- breaking large text into **smaller pieces**
- making it easier for AI systems to process and search

Example:
- Full document → too large and messy
- Chunks → smaller, focused, searchable parts

---

### 2. Why Chunking Matters in RAG
RAG systems do **not** usually send an entire document to the AI.

Instead they:
1. Split the document into chunks
2. Convert chunks into embeddings
3. Search the most relevant chunks
4. Send only the best chunks to the AI

This makes answers:
- more accurate
- more relevant
- faster

---

### 3. Character-Based Chunking
In this project, text is split by **character length**.

Example:
- Chunk size = 500 characters
- Large text is divided every 500 characters

This is the simplest form of chunking and a strong foundation for learning RAG.

---
# Day 26 — Retrieval System for RAG

## 🎯 Goal
Build the **retrieval layer** of a RAG (Retrieval-Augmented Generation) system by:
- converting document chunks into embeddings
- storing them in FAISS
- retrieving the most relevant chunks for a user’s question

---

## 🧠 Concepts Learned

### 1. What is Retrieval?
Retrieval means:
- searching a document for the **most relevant pieces of information**
- finding context **before** asking an AI model to answer

Instead of sending the entire document to the AI, we first retrieve only the best-matching chunks.

---

### 2. Query Embedding
A user question is converted into an **embedding vector**.

This allows the system to compare:
- the question vector
- the chunk vectors

and retrieve the chunks with the closest meaning.

---

### 3. FAISS Vector Search
FAISS is used as a **vector database** to:
- store chunk embeddings
- perform fast similarity search

This enables semantic search instead of basic keyword matching.

---

### 4. Top-k Retrieval
The system returns the **top matching chunks** for a question.

In this project:
- `k = min(3, len(chunks))`

This ensures the system only asks FAISS for a valid number of results.

---

### 5. Distance Score
FAISS returns a **distance score** for each result.

Using `IndexFlatL2`:
- **smaller distance = better match**
- larger distance = weaker match

This helps measure how relevant each chunk is to the user’s question.

---

# Day 27 — RAG Document Q&A System

## 🎯 Goal
Build a complete **Retrieval-Augmented Generation (RAG)** pipeline that can:
- read a document
- retrieve the most relevant chunks
- send them to OpenAI
- generate a final answer grounded in the document

---

## 🧠 Concepts Learned

### 1. What is RAG?
RAG stands for:

**Retrieval-Augmented Generation**

It combines:
- **Retrieval** → finding the most relevant document chunks
- **Generation** → using an LLM to answer based on those chunks

This allows AI systems to answer from **your own data** instead of relying only on built-in knowledge.

---

### 2. Context Injection
Instead of asking the AI a question directly, we first provide it with the **most relevant context** retrieved from the document.

Example:

```text id="7kthh8"
Context:
[retrieved chunks]

Question:
What skills are mentioned?


# Day 28 — Multi-PDF Career RAG Assistant

## 🎯 Goal
Build a **multi-document Retrieval-Augmented Generation (RAG)** system that can:
- read multiple PDF files
- extract and combine their content
- retrieve relevant chunks using semantic search
- answer career-related questions using OpenAI

This project upgrades a basic single-document chatbot into a **career-focused AI assistant** powered by multiple PDFs.

---

## 🧠 Concepts Learned

### 1. What is Multi-Document RAG?
Multi-Document RAG allows an AI system to answer questions using **multiple source documents**, not just one.

Instead of asking questions about a single resume, this system can search across:
- a resume
- multiple internship/job descriptions
- career-related PDFs

This makes the assistant more realistic and more useful.

---

### 2. Multi-Document Ingestion
The system automatically reads every PDF inside the `documents/` folder.

This means:
- no hardcoded file names
- easy scalability
- professional project structure

This is similar to how real-world document AI systems ingest knowledge bases.

---

### 3. Semantic Search Across Documents
Each chunk of text is converted into an embedding and stored in **FAISS**.

This allows the system to retrieve information by **meaning**, not just keyword matching.

---

### 4. Career-Focused AI Assistant
The system is designed to answer questions such as:
- What skills appear most often across these job descriptions?
- Which skills in my resume match these roles?
- What keywords seem missing from my resume?
- What should I learn next to better fit these jobs?

This turns the project into a useful **career intelligence assistant**.

---


```bash


