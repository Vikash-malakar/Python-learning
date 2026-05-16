print("Word Counter")

text = input("Enter a sentence: ")

words = text.split()

word_count = len(words)
char_count = len(text)

vowel_count = 0

for ch in text.lower():
    if ch in "aeiou":
        vowel_count += 1

print("\nResult")
print("Total Words:", word_count)
print("Total Characters:", char_count)
print("Total Vowels:", vowel_count)