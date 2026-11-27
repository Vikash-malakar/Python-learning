# Day 01: List, Dictionary and Set Comprehension

# 1. List Comprehension
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squares = [num ** 2 for num in numbers]

print("Squares:", squares)


# 2. Even Numbers
even_numbers = [num for num in numbers if num % 2 == 0]

print("Even Numbers:", even_numbers)


# 3. Dictionary Comprehension
square_dict = {num: num ** 2 for num in numbers}

print("Dictionary:", square_dict)


# 4. Set Comprehension
unique_squares = {num ** 2 for num in numbers}

print("Set:", unique_squares)


# 5. Nested List Comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

flattened = [num for row in matrix for num in row]

print("Flattened List:", flattened)