questions = [
    {
        "question": "Which language is used for Python programming?",
        "options": ["Python", "HTML", "CSS", "SQL"],
        "answer": "1"
    },
    {
        "question": "What does CPU stand for?",
        "options": [
            "Central Processing Unit",
            "Computer Personal Unit",
            "Central Program Utility",
            "Control Processing Unit"
        ],
        "answer": "1"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["//", "#", "/*", "<!--"],
        "answer": "2"
    },
    {
        "question": "Which data type stores True or False?",
        "options": ["String", "Integer", "Boolean", "List"],
        "answer": "3"
    }
]


def start_quiz():
    score = 0

    print("\n" + "=" * 50)
    print("               🧠 QUIZ GAME")
    print("=" * 50)

    for number, question in enumerate(questions, 1):
        print(f"\nQ{number}. {question['question']}")

        for index, option in enumerate(question["options"], 1):
            print(f"{index}. {option}")

        answer = input("Your answer: ").strip()

        if answer == question["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            print("❌ Wrong!")

    print("\n" + "=" * 50)
    print(f"🏆 Final Score: {score}/{len(questions)}")
    print("=" * 50)


if __name__ == "__main__":
    start_quiz()