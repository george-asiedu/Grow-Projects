from datetime import date
import tkinter as tk
from tkinter import messagebox

user_pin = 5566
name = ''
balance = 0.0
transactions = []
current_date = date.today()


class ATMSimulator:
    def __init__(self, master):
        self.master = master
        self.master.title("ATM Simulator System")
        self.master.geometry("600x600")
        self.main_frame = tk.Frame(master)
        self.main_frame.pack()
        self.introduction_frame()

    def introduction_frame(self):
        self.clear_frame()
        tk.Label(self.main_frame, text="Welcome to MEST ATM System").pack(pady=10)

        self.name_entry = tk.Entry(self.main_frame)
        self.name_entry.pack(pady=5)
        self.name_entry.insert(0, "Enter your name")

        tk.Button(self.main_frame, text="Submit", command=self.auth_frame).pack(pady=10)

    def auth_frame(self):
        global name
        name = self.name_entry.get()
        self.clear_frame()

        tk.Label(self.main_frame, text=f"Hello {name}, please enter your PIN").pack(pady=10)

        self.pin_entry = tk.Entry(self.main_frame, show='*')
        self.pin_entry.pack(pady=5)

        tk.Button(self.main_frame, text="Submit", command=self.check_pin).pack(pady=10)

    def check_pin(self):
        user_input = self.pin_entry.get()

        if user_input.isdigit() and int(user_input) == user_pin:
            self.menu_frame()
        else:
            messagebox.showerror("Error", "Incorrect PIN. Please try again.")
            self.introduction_frame()

    def menu_frame(self):
        self.clear_frame()
        tk.Label(self.main_frame, text="ATM Menu").pack(pady=10)

        tk.Button(self.main_frame, text="Deposit Cash", command=self.deposit_cash_frame).pack(pady=5)
        tk.Button(self.main_frame, text="Check Balance", command=self.check_balance).pack(pady=5)
        tk.Button(self.main_frame, text="Withdraw Cash", command=self.withdraw_cash_frame).pack(pady=5)
        tk.Button(self.main_frame, text="Transactions History", command=self.transactions_history).pack(pady=5)
        tk.Button(self.main_frame, text="Exit ATM", command=self.exit_atm).pack(pady=5)

    def deposit_cash_frame(self):
        self.clear_frame()
        tk.Label(self.main_frame, text="Enter amount to deposit").pack(pady=10)

        self.deposit_entry = tk.Entry(self.main_frame)
        self.deposit_entry.pack(pady=5)

        tk.Button(self.main_frame, text="Submit", command=self.deposit_cash).pack(pady=10)
        tk.Button(self.main_frame, text="Back", command=self.menu_frame).pack(pady=5)

    def deposit_cash(self):
        amount = self.deposit_entry.get()
        if not amount.replace('.', '', 1).isdigit() or float(amount) <= 0:
            messagebox.showerror("Error", "Invalid amount. Please enter a positive number.")
            return

        amount = float(amount)
        global balance
        balance += amount
        transactions.append(f"Deposited: ${amount}, Timestamp: {current_date}")

        receipt_choice = messagebox.askyesno("Receipt", "Would you like a receipt?")
        if receipt_choice:
            self.print_receipt(amount, 'Deposit')

        messagebox.showinfo("Success", f"You have successfully deposited GHC{amount}.")
        self.menu_frame()

    def check_balance(self):
        messagebox.showinfo("Balance", f"Your current balance is GHC{balance}.")
        self.menu_frame()

    def withdraw_cash_frame(self):
        self.clear_frame()
        tk.Label(self.main_frame, text="Enter amount to withdraw").pack(pady=10)

        self.withdraw_entry = tk.Entry(self.main_frame)
        self.withdraw_entry.pack(pady=5)

        tk.Button(self.main_frame, text="Submit", command=self.withdraw_cash).pack(pady=10)
        tk.Button(self.main_frame, text="Back", command=self.menu_frame).pack(pady=5)

    def withdraw_cash(self):
        amount = self.withdraw_entry.get()
        if not amount.replace('.', '', 1).isdigit() or float(amount) <= 0:
            messagebox.showerror("Error", "Invalid amount. Please enter a positive number.")
            return

        amount = float(amount)
        global balance
        withdraw_limit = 5000

        if amount > balance:
            messagebox.showerror("Error", "Insufficient funds. Please try a smaller amount.")
            return

        if amount > withdraw_limit:
            messagebox.showerror("Error",
                                 f"Withdrawal limit exceeded. Please enter an amount less than or equal to GHC{withdraw_limit}.")
            return

        balance -= amount
        transactions.append(f"Withdrew: ${amount}, Timestamp: {current_date}")

        receipt_choice = messagebox.askyesno("Receipt", "Would you like a receipt?")
        if receipt_choice:
            self.print_receipt(amount, 'Withdraw')

        messagebox.showinfo("Success", f"You have successfully withdrawn GHC{amount}.")
        self.menu_frame()

    def transactions_history(self):
        if not transactions:
            messagebox.showinfo("History", "No transactions available.")
        else:
            history = "\n".join(transactions)
            messagebox.showinfo("Transaction History", history)
        self.menu_frame()

    def print_receipt(self, amount, transaction_type):
        receipt_text = (
            f"\n--------------------------\n"
            f"ATM RECEIPT\n"
            f"Transaction: {transaction_type}\n"
            f"Name: {name}\n"
            f"Amount: {amount}\n"
            f"Balance: {balance}\n"
            f"Date: {current_date}\n"
            f"--------------------------"
        )
        messagebox.showinfo("Receipt", receipt_text)

    def exit_atm(self):
        messagebox.showinfo("Goodbye", "Thank you for using the MEST ATM system. Goodbye!")
        self.master.quit()

    def clear_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = ATMSimulator(root)
    root.mainloop()