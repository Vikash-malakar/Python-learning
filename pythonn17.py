# Day 17: Property Decorators

class Product:

    def __init__(self, name, price):
        self.name = name
        self._price = price

    # Getter
    @property
    def price(self):
        return self._price

    # Setter
    @price.setter
    def price(self, value):

        if value > 0:
            self._price = value

        else:
            raise ValueError("Price must be positive")

    # Deleter
    @price.deleter
    def price(self):
        del self._price


product = Product("Laptop", 50000)

print("Product:", product.name)

print("Price:", product.price)

product.price = 60000

print("Updated Price:", product.price)