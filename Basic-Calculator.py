number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
operation = input("Enter (+) for Addition, (-) for Subtraction, (*) for Multiplication, (/) for Division: ")

if operation == "+":
    result = number1 + number2
    print("Sum:", result)
elif operation == "-":
    result = number1 - number2
    print("Difference:", result)
elif operation == "*":
    result = number1 * number2
    print("Product:", result)
elif operation == "/":
    if number2 != 0:
        result = number1 / number2
        print("Quotient:", result)
    else:
        print("Error: Division by zero is not allowed!")
else:
    print("Error: Invalid operation entered.")

