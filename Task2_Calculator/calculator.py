

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return None
    return a / b


def calculator():
    print("\n========== PYTHON CALCULATOR ==========")

    while True:
        print("\nSelect an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == "5":
            print("Thank you for using the calculator!")
            break

        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice! Please select between 1 and 5.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            continue

        if choice == "1":
            result = add(num1, num2)
            operator = "+"

        elif choice == "2":
            result = subtract(num1, num2)
            operator = "-"

        elif choice == "3":
            result = multiply(num1, num2)
            operator = "*"

        else:
            result = divide(num1, num2)
            operator = "/"

            if result is None:
                print("Error! Division by zero is not allowed.")
                continue

        print(f"\nResult: {num1:g} {operator} {num2:g} = {result:g}")


if __name__ == "__main__":
    calculator()

