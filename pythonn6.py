# Day 06: Iterators in Python

# 1. Creating an Iterator

numbers = [10, 20, 30, 40, 50]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))


# 2. Custom Iterator

class MyNumbers:

    def __init__(self, limit):
        self.limit = limit
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):

        if self.current <= self.limit:
            value = self.current
            self.current += 1
            return value

        else:
            raise StopIteration


numbers = MyNumbers(5)

for num in numbers:
    print(num)


# 3. String Iterator

name = "PYTHON"

name_iterator = iter(name)

print(next(name_iterator))
print(next(name_iterator))
print(next(name_iterator))