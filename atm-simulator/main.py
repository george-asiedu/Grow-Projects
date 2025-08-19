from datetime import date
import tkinter as tk

user_pin = 5566
name = ''
choice = 0
balance = 0.0
transactions = []
current_date = date.today()
root = tk.Tk()

def open_window():
    global root
    root.title("ATM Simulator System")
    root.geometry("600x600")
    root.mainloop()

def introduction():
    global name
    user_input = input("What is your name: ")
    name = user_input
    print(f"\nHello {name}, welcome to the MEST ATM system.")

def auth_pin():
    while True:
        try:
            user_input = int(input("Enter your PIN: "))
            if user_input == user_pin:
                return True
            else:
                print("Incorrect PIN. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a numeric PIN.")

def show_menu():
    print("\nATM Menu:")
    print("1. Deposit Cash")
    print("2. Check Balance")
    print("3. Withdraw Cash")
    print("4. Transactions History")
    print("5. Exit ATM")

def menu_options():
    global choice
    show_menu()

    while True:
        try:
            choice = int(input("Select an option (1-5): "))
            if choice == 1:
                deposit_cash()
                show_menu()
            elif choice == 2:
                check_balance()
                show_menu()
            elif choice == 3:
                withdraw_cash()
                show_menu()
            elif choice == 4:
                transactions_history()
                show_menu()
            elif choice == 5:
                exit_atm()
            else:
                print("Invalid choice. Please select a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a numeric option.")

def deposit_cash():
    global balance
    print("Deposit cash.")
    print("-------------- \n")

    while True:
        try:
            receipt_choice = input("Would you like a receipt? (yes/no): ").strip().lower()
            amount = float(input("Enter the amount to deposit: "))
            transaction_type = 'Deposit'

            if amount <= 0:
                print("Invalid amount. Please enter a positive number.")
                continue

            balance += amount
            transactions.append(f"Deposited: ${amount}, Timestamp: {current_date}")

            if receipt_choice not in ['yes', 'no']:
                print("Invalid choice. Please enter 'yes' or 'no'.")
                continue

            if receipt_choice == 'yes':
                receipt(amount, transaction_type)
            else:
                print("Transaction completed without a receipt.")

            return amount, transaction_type

        except ValueError:
            print("Invalid input. Please enter a numeric amount.")

def check_balance():
    print(f"Your current balance is GHC{balance}.")

def withdraw_cash():
    global balance
    print("Withdrawn cash.")
    print("-------------- \n")

    while True:
        try:
            receipt_choice = input("Would you like a receipt? (yes/no): ").strip().lower()
            amount = float(input("Enter the amount to withdraw: "))
            transaction_type = 'Withdraw'
            withdraw_limit = 5000

            if amount > balance:
                print("Insufficient funds. Please try a smaller amount.")
                continue

            elif amount <= 0:
                print("Invalid amount. Please enter a positive number.")
                continue

            elif amount > withdraw_limit:
                print(f"Withdrawal limit exceeded. Please enter an amount less than or equal to GHC{withdraw_limit}.")
                continue

            balance -= amount
            transactions.append(f"Withdrew: ${amount}, Timestamp: {current_date}")

            if receipt_choice not in ['yes', 'no']:
                print("Invalid choice. Please enter 'yes' or 'no'.")
                continue

            if receipt_choice == 'yes':
                receipt(amount, transaction_type)
            else:
                print("Transaction completed without a receipt.")

            return amount, transaction_type

        except ValueError:
            print("Invalid input. Please enter a numeric amount.")

def transactions_history():
    if not transactions:
        print("No transactions available.")
    else:
        print("Transaction History:")
        for transaction in transactions:
            print(transaction)

def receipt(amount, transaction_type):
    print("\n--------------------------")
    print("ATM RECEIPT")
    print(f"Transaction: {transaction_type}")
    print(f"Name: {name}")
    print(f"Amount: {amount}")
    print(f"Balance: {balance}")
    print(f"Date: {current_date}")
    print("\n--------------------------")

    if transaction_type == 'Withdraw':
        print(f"You have successfully withdrawn an amount of GHC{amount}. Your current balance is GHC{balance}.")
    elif transaction_type == 'Deposit':
        print(f"You have successfully deposited an amount of GHC{amount}. Your current balance is GHC{balance}.")

def exit_atm():
    print("Thank you for using the MEST ATM system. Goodbye!")
    exit()

def main():
    introduction()
    if auth_pin():
        print("Login successful! You can now access your account.")
    menu_options()

main()