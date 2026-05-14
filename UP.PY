print("Quiz Game")

score = 0

questions = [
    ["Python kis type ki language hai?", "high level"],
    ["5 + 7 = ?", "12"],
    ["India ki capital kya hai?", "delhi"],
    ["HTML ka full form kya hai?", "hyper text markup language"]
]

for q in questions:
    answer = input(q[0] + " ")

    if answer.lower() == q[1]:
        print("Correct Answer")
        score += 1
    else:
        print("Wrong Answer")

print("\nFinal Score:", score, "/", len(questions))

if score == len(questions):
    print("Excellent")
elif score >= 2:
    print("Good")
else:
    print("Need More Practice")