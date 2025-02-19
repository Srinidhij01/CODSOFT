def calculator():
    print("Simple Calculator")
    print("Operations: + (Addition), - (Subtraction), * (Multiplication), / (Division)")

    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operation (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                return
            result = num1 / num2
        else:
            print("Invalid operator! Please enter +, -, *, or /.")
            return

        print(f"Result: {num1} {operator} {num2} = {result}")

    except ValueError:
        print("Invalid input! Please enter numeric values.")

# Run the calculator
calculator()
