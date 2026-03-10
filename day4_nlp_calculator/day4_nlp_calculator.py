import re

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

print("Welcome to NLP Smart Calculator")
print("Type commands like: Add 5 and 3, Divide 10 by 2, or Exit")

while True:
    command = input("\nEnter your command: ").lower()
    
    if "exit" in command:
        print("Goodbye!")
        break

    # Clean command
    command = command.replace("by", "").replace("&", "and")

    try:
        numbers = re.findall(r"[-+]?\d*\.\d+|\d+", command)
        if len(numbers) < 2:
            raise ValueError("Please enter two numbers.")
        num1, num2 = float(numbers[0]), float(numbers[1])

        if "add" in command:
            result = add(num1, num2)
        elif "subtract" in command:
            result = subtract(num1, num2)
        elif "multiply" in command:
            result = multiply(num1, num2)
        elif "divide" in command:
            result = divide(num1, num2)
        else:
            result = "Command not recognized"

        print("Result:", result)

    except Exception as e:
        print("Error:", e)