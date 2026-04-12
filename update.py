print("=== To-Do List Manager 📋 ===")

tasks = []

while True:
    print("\n1. Add Task")
    print("2. Show Tasks")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter your task: ")
        tasks.append(task)
        print(" Task Added!")

    elif choice == "2":
        if len(tasks) == 0:
            print("📭 No tasks yet!")
        else:
            print("\n Your Tasks:")
            for i in range(len(tasks)):
                print(i + 1, "-", tasks[i])

    elif choice == "3":
        print("👋 Exiting... Bye!")
        break

    else:
        print(" Invalid Choice")