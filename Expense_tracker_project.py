import os

# Global list to store expenses
expenses = []

# Function to load expenses from file
def load_expenses():
    if os.path.exists("expenses.txt"):
        with open("expenses.txt", "r") as f:
            for line in f:
                date, category, amount, description = line.strip().split(",")
                expenses.append({
                    "date": date,
                    "category": category,
                    "amount": float(amount),
                    "description": description
                })

# Function to save expenses to file
def save_expenses():
    with open("expenses.txt", "w") as f:
        for exp in expenses:
            f.write(f"{exp['date']},{exp['category']},{exp['amount']},{exp['description']}\n")

# Function to add expense
def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (Food, Travel, Bills, etc.): ")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")

    expenses.append({
        "date": date,
        "category": category,
        "amount": amount,
        "description": description
    })
    save_expenses()
    print("✅ Expense added successfully!\n")

# Function to view all expenses
def view_expenses():
    if not expenses:
        print("No expenses recorded yet.")
        return
    print("\n📌 All Expenses:")
    for idx, exp in enumerate(expenses, start=1):
        print(f"{idx}. {exp['date']} - {exp['category']} - ₹{exp['amount']} - {exp['description']}")
    print()

# Function to calculate total expenses by category
def total_by_category():
    totals = {}
    for exp in expenses:
        totals[exp['category']] = totals.get(exp['category'], 0) + exp['amount']

    print("\n📊 Total Expenses by Category:")
    for cat, amt in totals.items():
        print(f"{cat}: ₹{amt}")
    print()

# Main menu
def main():
    load_expenses()
    while True:
        print("=== Expense Tracker ===")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Total by Category")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_by_category()
        elif choice == "4":
            print("💾 Saving and exiting...")
            save_expenses()
            break
        else:
            print("❌ Invalid choice, please try again.\n")

if __name__ == "__main__":
    main()
