# Day 15: Abstraction

from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class CreditCard(Payment):

    def pay(self, amount):
        print("Paid using Credit Card:", amount)


class UPI(Payment):

    def pay(self, amount):
        print("Paid using UPI:", amount)


class Cash(Payment):

    def pay(self, amount):
        print("Paid using Cash:", amount)


# Creating Objects

payment1 = CreditCard()
payment2 = UPI()
payment3 = Cash()

payment1.pay(5000)
payment2.pay(2000)
payment3.pay(1000)  