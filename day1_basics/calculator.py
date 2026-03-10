number1 = int(input("Enter number 1 "))
number2 = int(input("Enter number 2 "))


print(f"Addition is {number1 + number2}")
print(f"Subtraction is {number1 - number2}")
print(f"Multiplication is {number1 * number2}")

if number2 != 0:
    print(f"Division is {number1 / number2}")
else:
    print("Division by zero is not allowed")