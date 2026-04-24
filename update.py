print("=== Voting System ===")

votes = {
    "Rahul": 0,
    "Amit": 0,
    "Vikash": 0
}

while True:
    print("\n1. Cast Vote")
    print("2. Show Results")
    print("3. Show Winner")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print("\nCandidates:")
        for name in votes:
            print(name)

        candidate = input("Enter candidate name: ")

        if candidate in votes:
            votes[candidate] += 1
            print("Vote Casted Successfully")
        else:
            print("Invalid Candidate")

    elif choice == "2":
        print("\nVoting Results:")
        for name, count in votes.items():
            print(name, ":", count)

    elif choice == "3":
        winner = max(votes, key=votes.get)
        print("Winner is:", winner)

    elif choice == "4":
        print("Program Closed")
        break

    else:
        print("Invalid Choice")