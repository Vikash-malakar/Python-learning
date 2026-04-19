print("=== Quiz Game ===")

score = 0

q1 = input("1. Python kis type ki language hai? ")
if q1.lower() == "high level":
    score += 1

q2 = input("2. 5 + 3 = ")
if q2 == "8":
    score += 1

q3 = input("3. HTML ka full form kya hai? ")
if q3.lower() == "hyper text markup language":
    score += 1

q4 = input("4. India ki capital kya hai? ")
if q4.lower() == "delhi":
    score += 1

q5 = input("5. Python file extension kya hoti hai? ")
if q5.lower() == ".py":
    score += 1

print("\n=== Result ===")
print("Total Score:", score, "/ 5")

if score == 5:
    print("Excellent")
elif score >= 3:
    print("Good")
else:
    print("Need Practice")