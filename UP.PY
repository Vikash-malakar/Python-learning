print("Number Frequency Counter")

numbers = input("Enter numbers separated by space: ").split()

frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

print("\nFrequency Result")

for num, count in frequency.items():
    print(num, "appears", count, "times")