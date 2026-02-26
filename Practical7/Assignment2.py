#Lab Assignment-2

"""
Create a Menu Driven program for showing details of a Bank Account by implementaing different functions for the following:

a) Display the current Balance

b) Mechanism to Deposit an amount

c) Mechanism to Withdraw an amount
"""

balance = 1000.0  # Initial Balance


def display_balance():
    print(f"Current Balance: ₹{balance:.2f}")


def deposit():
    global balance
    amount = float(input("Enter amount to deposit: ₹"))

    if amount > 0:
        balance += amount
        print("Amount deposited successfully.")
    else:
        print("Invalid deposit amount.")


def withdraw():
    global balance
    amount = float(input("Enter amount to withdraw: ₹"))

    if amount <= 0:
        print("Invalid withdrawal amount.")
    elif amount > balance:
        print("Insufficient balance.")
    else:
        balance -= amount
        print("Amount withdrawn successfully.")


def main():
    while True:
        print("\n----- BANK MENU -----")
        print("1. Display Current Balance")
        print("2. Deposit Amount")
        print("3. Withdraw Amount")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            display_balance()

        elif choice == '2':
            deposit()

        elif choice == '3':
            withdraw()

        elif choice == '4':
            print("Thank you for banking with us.")
            break

        else:
            print("Invalid choice! Please select between 1-4.")


if __name__ == "__main__":
    main()