import csv
from datetime import datetime

# File to store expenses
FILE_NAME = "expenses.csv"

# Initialize CSV file if not exists
def init_file():
    try:
        with open(FILE_NAME, "x", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount", "Description"])
    except FileExistsError:
        pass

# Add a new expense
def add_expense(category, amount, description=""):
    try:
        amount = float(amount)  # validate amount
    except ValueError:
        print("❌ Amount must be a number!")
        return
    
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category.lower(), amount, description])
    print("✅ Expense added successfully!")

# View all expenses
def view_expenses():
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

# Get summary by category
def summary_by_category():
    categories = {}
    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            category = row["Category"].lower()   # সব ছোট হাতের
            amount = float(row["Amount"])
            categories[category] = categories.get(category, 0) + amount
    
    print("\n📊 Expense Summary by Category:")
    print("-" * 40)
    print(f"{'Category':<15}{'Total (₹)':>15}")
    print("-" * 40)
    for category, total in categories.items():
        print(f"{category:<15}{total:>15.2f}")
    print("-" * 40)

# Main menu
def main():
    init_file()
    while True:
        print("\n--- 💰 Expense Tracker ---")
        print("1️⃣ Add Expense")
        print("2️⃣ View Expenses")
        print("3️⃣ Summary by Category")
        print("4️⃣ Exit")
        
        choice = input("👉 Enter choice: ")
        
        if choice == "1":
            category = input("Enter category (Food, Travel, etc.): ")
            amount = input("Enter amount: ")
            description = input("Enter description (optional): ")
            add_expense(category, amount, description)
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            summary_by_category()
        elif choice == "4":
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice, try again.")

if __name__ == "__main__":
    main()
