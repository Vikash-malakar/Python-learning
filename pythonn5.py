# Day 05: Generators and Yield

# 1. Simple Generator

def generate_numbers():

    yield 1
    yield 2
    yield 3
    yield 4
    yield 5


for num in generate_numbers():
    print(num)


# 2. Generator with Loop

def square_generator(n):

    for i in range(1, n + 1):
        yield i ** 2


for square in square_generator(5):
    print("Square:", square)


# 3. Infinite Generator

def infinite_numbers():

    num = 1

    while True:
        yield num
        num += 1


generator = infinite_numbers()

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))


# 4. Fibonacci Generator

def fibonacci(n):

    a, b = 0, 1

    for i in range(n):
        yield a
        a, b = b, a + b


print("Fibonacci:", list(fibonacci(10)))