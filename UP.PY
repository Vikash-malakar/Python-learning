print("Palindrome Checker")

text = input("Enter a word or number: ")

reverse_text = text[::-1]

if text == reverse_text:
    print("Palindrome")
else:
    print("Not Palindrome")