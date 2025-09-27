import csv
from datetime import datetime

FILENAME = "expenses.csv"

# Add a new expense
def add_expense():
    date = input("Enter date (YYYY-MM-DD) or leave blank for today: ")
    if not date:
        date = datetime.today().strftime('%Y-%m-%d')
    category = input("Enter category: ")
    description = input("Enter description: ")
    amount = float(input("Enter amount: "))

    with open(FILENAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, description, amount])

    print(f"✅ Expense added: {date}, {category}, {description}, {amount}")

# View all expenses
def view_expenses():
    try:
        with open(FILENAME, "r") as file:
            reader = csv.reader(file)
            print("\nDate       | Category   | Description      | Amount")
            print("-"*50)
            for row in reader:
                print(f"{row[0]} | {row[1]:<10} | {row[2]:<15} | {row[3]}")
    except FileNotFoundError:
        print("⚠️ No expenses recorded yet.")

# Main menu
def main():
    while True:
        print("\n--- Expense Tracker Menu ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")

        choice = input("Enter choice: ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print("👋 Exiting Expense Tracker")
            break
        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    main()
