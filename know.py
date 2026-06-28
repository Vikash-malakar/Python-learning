sentence = input("Enter a sentence: ").lower()

alphabet = "abcdefghijklmnopqrstuvwxyz"

is_pangram = True

for letter in alphabet:
    if letter not in sentence:
        is_pangram = False
        break

if is_pangram:
    print("It is a Pangram")
else:
    print("It is not a Pangram")