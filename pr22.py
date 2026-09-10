import os
from collections import Counter


def count_extensions(folder):
    if not os.path.exists(folder):
        print("❌ Folder not found.")
        return

    if not os.path.isdir(folder):
        print("❌ Please enter a folder path.")
        return

    extensions = Counter()
    total_files = 0

    for root, directories, files in os.walk(folder):

        for file in files:
            total_files += 1

            extension = os.path.splitext(file)[1].lower()

            if extension:
                extensions[extension] += 1
            else:
                extensions["No Extension"] += 1

    print("\n" + "=" * 50)
    print("          📊 FILE EXTENSION COUNTER")
    print("=" * 50)

    print(f"\n📁 Folder: {folder}")
    print(f"📄 Total Files: {total_files}")

    print("\n📌 Extensions")
    print("-" * 35)

    if not extensions:
        print("No files found.")
        return

    for extension, count in extensions.most_common():
        print(f"{extension:<20} {count}")

    print("\n" + "=" * 50)


def main():
    folder = input(
        "Enter folder path: "
    ).strip()

    count_extensions(folder)


if __name__ == "__main__":
    main()