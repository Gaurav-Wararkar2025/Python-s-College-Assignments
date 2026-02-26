#Lab Assignment-1

"""
Create a Menu Driven application "CAL.C" by implemnting different functions for the following basic operations:

a) Addition

b) Subtraction

c) Multiplication

d) Division

e) Modulus
"""

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error! Division by zero is not allowed."
    return a / b

def modulus(a, b):
    if b == 0:
        return "Error! Modulus by zero is not allowed."
    return a % b


def main():
    while True:
        print("\n----- CALCULATOR MENU -----")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Modulus")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '6':
            print("Exiting Calculator...")
            break

        if choice in ['1', '2', '3', '4', '5']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print("Result =", addition(num1, num2))

            elif choice == '2':
                print("Result =", subtraction(num1, num2))

            elif choice == '3':
                print("Result =", multiplication(num1, num2))

            elif choice == '4':
                print("Result =", division(num1, num2))

            elif choice == '5':
                print("Result =", modulus(num1, num2))

        else:
            print("Invalid choice! Please select between 1-6.")


if __name__ == "__main__":
    main()