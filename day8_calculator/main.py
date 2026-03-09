from operations import add, subtract, multiply, divide
from history import save_history, view_history


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

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            continue

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
        view_history()

    else:
        print("Invalid option. Please choose a number between 1 and 6.")