# Day 14: Encapsulation

class BankAccount:

    def __init__(self, account_holder, balance):

        self.account_holder = account_holder
        self.__balance = balance

    # Getter
    def get_balance(self):
        return self.__balance

    # Deposit Method
    def deposit(self, amount):

        if amount > 0:
            self.__balance += amount
            print("Amount Deposited:", amount)

        else:
            print("Invalid Amount")

    # Withdraw Method
    def withdraw(self, amount):

        if amount <= 0:
            print("Invalid Amount")

        elif amount <= self.__balance:
            self.__balance -= amount
            print("Amount Withdrawn:", amount)

        else:
            print("Insufficient Balance")


account = BankAccount("Vikash", 10000)

print("Initial Balance:", account.get_balance())

account.deposit(5000)

account.withdraw(2000)

print("Final Balance:", account.get_balance())