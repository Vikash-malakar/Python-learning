class ModelRegistry(type):

    registry = {}

    def __new__(mcs, name, bases, namespace):

        cls = super().__new__(
            mcs, name, bases, namespace
        )

        if name != "BaseModel":
            mcs.registry[name] = cls

        return cls


class BaseModel(metaclass=ModelRegistry):
    pass


class User(BaseModel):
    def __init__(self, username):
        self.username = username


class Product(BaseModel):
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Order(BaseModel):
    pass


print("Registered Models:")

for model_name, model_class in ModelRegistry.registry.items():
    print(model_name, "->", model_class)

print("\nCreate Dynamic Object:")

user = ModelRegistry.registry["User"]("Vikash")
print(user.username)