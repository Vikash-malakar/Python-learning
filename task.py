text = input("Enter a sentence: ").lower()

frequency = {}

for ch in text:
    if ch != " ":
        if ch in frequency:
            frequency[ch] += 1
        else:
            frequency[ch] = 1

for ch, count in frequency.items():
    print(ch, ":", count)
    print("Final")