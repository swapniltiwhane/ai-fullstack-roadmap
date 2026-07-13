# Finance tracker application
print("==============================")
print("Finance Tracker")
print("==============================")
print("\n 1. Add Income\n 2. Add Expense\n 3. View Balance\n 4. View Transaction\n 5. Monthly Summary\n 6. Exit \n");
transactions = []
def add_income():
    category = input("Enter income category: ")
    amount = float(input("Enter income amount: "))
    transaction = {"type": "income", "category": category, "amount": amount}
    transactions.append(transaction)
    print("Income added successfully!")

def add_expense():
    category = input("Enter expense category: ")
    amount = float(input("Enter expense amount: "))
    transaction = {"type": "expense", "category": category, "amount": amount}
    transactions.append(transaction)
    print("Expense added successfully!")

def view_balance():
    total_income = sum(txn["amount"] for txn in transactions if txn["type"] == "income")
    total_expense = sum(txn["amount"] for txn in transactions if txn["type"] == "expense")
    balance = total_income - total_expense
    print(f"Current Balance: ${balance:.2f}")

def view_transactions():
    for txn in transactions:
        print(f"{txn['type'].capitalize()}: {txn['category']} - ${txn['amount']:.2f}")

def calculate_balance():
    total_income = sum(txn["amount"] for txn in transactions if txn["type"] == "income")
    total_expense = sum(txn["amount"] for txn in transactions if txn["type"] == "expense")
    return total_income, total_expense

def monthly_summary():
    income,expense = calculate_balance()
    print("\n ---------------Balance---------------")
    print(f"Total Income: ${income:.2f}")
    print(f"Total Expense: ${expense:.2f}")
    print(f"Net Balance: ${income - expense:.2f}")

choice = 0
while choice != 'Exit':
    choice = input("Enter your choice: ")
    if choice == '1':
        add_income()
    elif choice == '2':
        add_expense()
    elif choice == '3':
        view_balance()
    elif choice == '4':
        view_transactions()
    elif choice == '5':
        monthly_summary()
    elif choice == '6':
        print("Exiting Finance Tracker. Goodbye!")
        break