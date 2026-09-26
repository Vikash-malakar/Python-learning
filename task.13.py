import os


def search_in_files(folder, keyword):
    if not os.path.isdir(folder):
        print("❌ Folder not found.")
        return

    found = False

    print("\n🔍 Searching...\n")

    for root, directories, files in os.walk(folder):

        for file_name in files:

            if not file_name.lower().endswith(".txt"):
                continue

            path = os.path.join(root, file_name)

            try:
                with open(
                    path,
                    "r",
                    encoding="utf-8"
                ) as file:
                    lines = file.readlines()

                for line_number, line in enumerate(lines, 1):

                    if keyword.lower() in line.lower():
                        print(
                            f"📄 {path} "
                            f"(Line {line_number})"
                        )
                        print(f"   {line.strip()}")
                        print()

                        found = True

            except (UnicodeDecodeError, PermissionError):
                continue

    if not found:
        print("❌ Keyword not found.")


def main():
    folder = input("Folder path: ").strip()
    keyword = input("Search keyword: ").strip()

    if not keyword:
        print("❌ Keyword required.")
        return

    search_in_files(folder, keyword)


if __name__ == "__main__":
    main()