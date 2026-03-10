# Day 7 - Calculator with History

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b


history_file = "calc_history.txt"


def save_history(text):
    with open(history_file, "a") as file:
        file.write(text + "\n")


while True:
    print("\nCalculator Menu")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. View History")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "6":
        print("Goodbye!")
        break

    elif choice in ["1", "2", "3", "4"]:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
            result = add(num1, num2)
            text = f"{num1} + {num2} = {result}"

        elif choice == "2":
            result = subtract(num1, num2)
            text = f"{num1} - {num2} = {result}"

        elif choice == "3":
            result = multiply(num1, num2)
            text = f"{num1} * {num2} = {result}"

        elif choice == "4":
            result = divide(num1, num2)
            text = f"{num1} / {num2} = {result}"

        print("Result:", result)
        save_history(text)

    elif choice == "5":
        try:
            with open(history_file, "r") as file:
                print("\n--- Calculation History ---")
                print(file.read())
        except FileNotFoundError:
            print("No history found yet.")