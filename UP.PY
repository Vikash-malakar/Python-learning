balance = 5000

def check_balance():
    print("Current Balance:", balance)

def deposit():
    global balance

    amount = float(input("Enter Deposit Amount: "))
    balance += amount

    print("Amount Deposited Successfully")

def withdraw():
    global balance

    amount = float(input("Enter Withdraw Amount: "))

    if amount <= balance:
        balance -= amount
        print("Amount Withdrawn Successfully")
    else:
        print("Insufficient Balance")

while True:

    print("\n===== ATM MACHINE =====")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        check_balance()

    elif choice == "2":
        deposit()

    elif choice == "3":
        withdraw()

    elif choice == "4":
        print("Thank You")
        break

    else:
        print("Invalid Choice")