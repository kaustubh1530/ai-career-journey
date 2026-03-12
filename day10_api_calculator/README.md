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

    JSON
    {"result": 8}


Multiply:
http://127.0.0.1:5000/multiply?a=6&b=7

    JSON
    {"result": 42}

Subtract:
http://127.0.0.1:5000/subtract?a=10&b=4

    JSON
    {"result": 6}

Divide:
http://127.0.0.1:5000/divide?a=20&b=5

    JSON
    {"result": 4}

## Technologies Used
- Python
- Flask
- REST API