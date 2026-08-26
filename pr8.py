import json
import os
from datetime import datetime


FILE_NAME = "tasks.json"


def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)

    except (json.JSONDecodeError, OSError):
        return []


def save_tasks(tasks):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4)


def add_task(tasks):
    print("\n--- ➕ ADD TASK ---")

    title = input("Enter task: ").strip()

    if not title:
        print("❌ Task cannot be empty.")
        return

    task = {
        "id": len(tasks) + 1,
        "title": title,
        "completed": False,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M")
    }

    tasks.append(task)
    save_tasks(tasks)

    print("✅ Task added successfully!")


def view_tasks(tasks):
    print("\n--- 📋 YOUR TASKS ---")

    if not tasks:
        print("No tasks found.")
        return

    for task in tasks:

        status = "✅ Done" if task["completed"] else "⏳ Pending"

        print(
            f"{task['id']}. "
            f"{task['title']} | "
            f"{status}"
        )


def complete_task(tasks):
    print("\n--- ✅ COMPLETE TASK ---")

    if not tasks:
        print("No tasks available.")
        return

    view_tasks(tasks)

    try:
        task_id = int(input("\nEnter task ID: "))
    except ValueError:
        print("❌ Enter a valid task ID.")
        return

    for task in tasks:

        if task["id"] == task_id:

            if task["completed"]:
                print("ℹ️ Task is already completed.")
            else:
                task["completed"] = True
                save_tasks(tasks)

                print("🎉 Task completed!")

            return

    print("❌ Task not found.")


def delete_task(tasks):
    print("\n--- 🗑️ DELETE TASK ---")

    if not tasks:
        print("No tasks available.")
        return

    view_tasks(tasks)

    try:
        task_id = int(input("\nEnter task ID: "))
    except ValueError:
        print("❌ Enter a valid task ID.")
        return

    for task in tasks:

        if task["id"] == task_id:

            tasks.remove(task)

            # IDs ko dobara arrange karo
            for index, task in enumerate(tasks, start=1):
                task["id"] = index

            save_tasks(tasks)

            print("🗑️ Task deleted successfully!")
            return

    print("❌ Task not found.")


def clear_completed(tasks):
    print("\n--- 🧹 CLEAR COMPLETED TASKS ---")

    remaining_tasks = [
        task for task in tasks
        if not task["completed"]
    ]

    deleted = len(tasks) - len(remaining_tasks)

    if deleted == 0:
        print("ℹ️ No completed tasks found.")
        return

    for index, task in enumerate(remaining_tasks, start=1):
        task["id"] = index

    tasks.clear()
    tasks.extend(remaining_tasks)

    save_tasks(tasks)

    print(f"🧹 {deleted} completed task(s) removed.")


def main():

    tasks = load_tasks()

    while True:

        print("\n" + "=" * 45)
        print("             📝 TO-DO LIST")
        print("=" * 45)

        print("1. ➕ Add Task")
        print("2. 📋 View Tasks")
        print("3. ✅ Complete Task")
        print("4. 🗑️ Delete Task")
        print("5. 🧹 Clear Completed")
        print("6. 🚪 Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            complete_task(tasks)

        elif choice == "4":
            delete_task(tasks)

        elif choice == "5":
            clear_completed(tasks)

        elif choice == "6":
            print("\n👋 Goodbye!")
            break

        else:
            print("❌ Invalid choice.")


if __name__ == "__main__":
    main()