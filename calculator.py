# Calculator CLI App

# Function for addition
def add(a, b):
    return a + b

# Function for subtraction
def subtract(a, b):
    return a - b

# Function for multiplication
def multiply(a, b):
    return a * b

# Function for division
def divide(a, b):
    if b == 0:
        return "Error! Division by zero is not allowed."
    return a / b


# Main loop
while True:
    print("\n===== Calculator Menu =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    # Exit condition
    if choice == '5':
        print("Calculator Closed.")
        break

    # Check valid choice
    if choice in ['1', '2', '3', '4']:

        # Take user input
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        # Perform operation
        if choice == '1':
            print("Result:", add(num1, num2))

        elif choice == '2':
            print("Result:", subtract(num1, num2))

        elif choice == '3':
            print("Result:", multiply(num1, num2))

        elif choice == '4':
            print("Result:", divide(num1, num2))

    else:
        print("Invalid choice! Please select between 1 and 5.")