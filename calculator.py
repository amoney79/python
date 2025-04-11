def main():
    # Ask for two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Ask for the operation
    operation = input("Enter the operation (+, -, *, /): ")

    # Perform calculation based on the operation
    if operation == "+":
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif operation == "-":
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    elif operation == "*":
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    elif operation == "/":
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
    else:
        print("Invalid operation. Please enter one of: +, -, *, /")

# Run the main function
if __name__ == "__main__":
    main()
