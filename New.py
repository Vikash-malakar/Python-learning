text = input("Enter a sentence: ").lower()

count = 0

for ch in text:
    if ch in "aeiou":
        count += 1

print("Total vowels:", count)
print("Total vowels:", count)