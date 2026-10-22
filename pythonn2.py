# Day 02: Lambda, Map, Filter and Reduce

from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1. Lambda Function
square = lambda x: x ** 2

print("Square:", square(5))


# 2. Map Function
squares = list(map(lambda x: x ** 2, numbers))

print("Squares:", squares)


# 3. Filter Function
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print("Even Numbers:", even_numbers)


# 4. Reduce Function
total = reduce(lambda x, y: x + y, numbers)

print("Sum:", total)


# 5. Find Maximum Using Reduce
maximum = reduce(lambda x, y: x if x > y else y, numbers)

print("Maximum:", maximum)