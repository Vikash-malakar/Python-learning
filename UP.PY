print("To Do List")

tasks = []

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task Added")

    elif choice == "2":
        print("\nYour Tasks")

        if len(tasks) == 0:
            print("No Tasks Found")
        else:
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])

    elif choice == "3":
        if len(tasks) == 0:
            print("No Tasks To Delete")

        else:
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])

            delete_task = int(input("Enter task number to delete: "))

            if delete_task > 0 and delete_task <= len(tasks):
                removed = tasks.pop(delete_task - 1)
                print("Deleted Task:", removed)
            else:
                print("Invalid Task Number")

    elif choice == "4":
        print("Program Closed")
        break

    else:
        print("Invalid Choice")