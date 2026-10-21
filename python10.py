class PositiveNumber:

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self

        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):

        if not isinstance(value, (int, float)):
            raise TypeError("Value must be numeric.")

        if value <= 0:
            raise ValueError("Value must be positive.")

        instance.__dict__[self.name] = value


class Product:

    price = PositiveNumber()
    quantity = PositiveNumber()

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        return self.price * self.quantity


product = Product("Laptop", 50000, 2)

print("Product:", product.name)
print("Price:", product.price)
print("Quantity:", product.quantity)
print("Total:", product.total_price())

# Test validation
# product.price = -100