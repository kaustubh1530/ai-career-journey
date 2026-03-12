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
 
```bash


