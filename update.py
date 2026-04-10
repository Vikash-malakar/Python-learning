print("=== Welcome to ATM  ===")

balance = 1000  # Initial balance

print("1. Check Balance")
print("2. Deposit")
print("3. Withdraw")

choice = int(input("Enter your choice (1-3): "))

if choice == 1:
    print(" Your Balance is:", balance)

elif choice == 2:
    amount = float(input("Enter amount to deposit: "))
    balance += amount
    print(" Deposited Successfully!")
    print(" New Balance:", balance)

elif choice == 3:
    amount = float(input("Enter amount to withdraw: "))
    
    if amount > balance:
        print(" Insufficient Balance!")
    else:
        balance -= amount
        print(" Withdrawal Successful!")
        print(" Remaining Balance:", balance)

else:
    print(" Invalid Choice")