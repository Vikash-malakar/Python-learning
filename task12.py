import json
import os

FILE_NAME = "notes.json"


def load_notes():
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except:
        return []


def save_notes(notes):
    with open(FILE_NAME, "w") as file:
        json.dump(notes, file, indent=4)


def add_note(notes):
    title = input("\nTitle: ").strip()
    content = input("Content: ").strip()

    if not title or not content:
        print("❌ Title and content required.")
        return

    notes.append({
        "title": title,
        "content": content
    })

    save_notes(notes)
    print("✅ Note saved!")


def show_notes(notes):
    if not notes:
        print("\n❌ No notes.")
        return

    for index, note in enumerate(notes, 1):
        print(f"\n{index}. {note['title']}")
        print(f"   {note['content']}")


def search_notes(notes):
    keyword = input("\nSearch: ").strip().lower()

    found = False

    for note in notes:
        if (
            keyword in note["title"].lower()
            or keyword in note["content"].lower()
        ):
            print(f"\n📝 {note['title']}")
            print(note["content"])
            found = True

    if not found:
        print("❌ No matching notes.")


def main():
    notes = load_notes()

    while True:
        print("\n" + "=" * 40)
        print("             📝 NOTES MANAGER")
        print("=" * 40)

        print("1. Add Note")
        print("2. View Notes")
        print("3. Search Notes")
        print("4. Exit")

        choice = input("\nChoice: ")

        if choice == "1":
            add_note(notes)
        elif choice == "2":
            show_notes(notes)
        elif choice == "3":
            search_notes(notes)
        elif choice == "4":
            break
        else:
            print("❌ Invalid choice.")


if __name__ == "__main__":
    main()