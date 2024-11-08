import csv
from datetime import datetime

# File to store expenses
EXPENSE_FILE = "expenses.csv"

# 1. Function to add an expense
def add_expense():
    date = datetime.now().strftime("%Y-%m-%d")
    amount = input("Enter amount: ")
    category = input("Enter category (e.g., food, travel, shopping): ")
    description = input("Enter a description: ")
    
    with open(EXPENSE_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, amount, category, description])
    
    print("Expense added successfully!")

# 2. Function to view expenses
def view_expenses():
    print("\nYour Expenses:")
    with open(EXPENSE_FILE, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            date, amount, category, description = row
            print(f"Date: {date}, Amount: {amount}, Category: {category}, Description: {description}")

# 3. Function to delete expenses
def delete_expense():
    view_expenses()  # Show all expenses to the user
    expenses = []

    # Load all expenses
    with open(EXPENSE_FILE, mode='r') as file:
        reader = csv.reader(file)
        expenses = list(reader)
    
    # Ask the user which expense to delete
    expense_index = int(input("Enter the expense number to delete: ")) - 1
    if 0 <= expense_index < len(expenses):
        del expenses[expense_index]
        
        # Write updated expenses to the file
        with open(EXPENSE_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(expenses)
        print("Expense deleted successfully!")
    else:
        print("Invalid selection.")

# 4. Main Menu Function
def main():
    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            delete_expense()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid option, please try again.")

# Run the application
main()
