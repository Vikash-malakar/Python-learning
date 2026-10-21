import inspect

class DataProcessor:
    def __init__(self, name, version):
        self.name = name
        self.version = version

    def process(self, data):
        return [item.upper() for item in data]


processor = DataProcessor("TextEngine", "2.0")

# Runtime introspection
print("Class:", processor.__class__.__name__)
print("Attributes:", vars(processor))
print("Methods:", inspect.getmembers(
    processor,
    predicate=inspect.ismethod
))

# Dynamic method inspection
method = getattr(processor, "process")
print("Method signature:", inspect.signature(method))

print(method(["python", "numpy", "pandas"]))