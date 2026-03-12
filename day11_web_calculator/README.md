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

## Running the Application

### 1. Navigate to the project folder

```bash
cd day11_web_calculator