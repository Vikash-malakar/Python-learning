questions = {
    "Python kis type ki language hai?": "high level",
    "2 + 2 = ?": "4",
    "India ki capital kya hai?": "delhi",
    "HTML ka full form kya hai?": "hyper text markup language",
    "5 * 6 = ?": "30"
}

score = 0

print("===== ONLINE EXAM SYSTEM =====")

for question, answer in questions.items():

    user_answer = input("\n" + question + " ")

    if user_answer.lower() == answer.lower():
        print("Correct Answer")
        score += 1
    else:
        print("Wrong Answer")

print("\n===== RESULT =====")
print("Score:", score, "/", len(questions))

percentage = (score / len(questions)) * 100

print("Percentage:", percentage, "%")

if percentage >= 80:
    print("Grade: A")

elif percentage >= 60:
    print("Grade: B")

elif percentage >= 40:
    print("Grade: C")

else:
    print("Grade: Fail")