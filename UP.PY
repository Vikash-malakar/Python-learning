print("Number Analysis Tool")

numbers = input("Enter numbers separated by space: ").split()

numbers = [int(num) for num in numbers]

total = sum(numbers)
average = total / len(numbers)

largest = max(numbers)
smallest = min(numbers)

even_count = 0
odd_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("\nAnalysis Result")
print("Numbers:", numbers)
print("Total:", total)
print("Average:", average)
print("Largest:", largest)
print("Smallest:", smallest)
print("Even Numbers:", even_count)
print("Odd Numbers:", odd_count)