sentence = input("Enter a sentence: ")

words = sentence.split()

reversed_words = words[::-1]

result = " ".join(reversed_words)

print("Reversed Sentence:", result)
print("-------------------logout---------------")