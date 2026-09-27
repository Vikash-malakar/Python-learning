import os


def calculate_size(folder):
    total_size = 0

    for root, directories, files in os.walk(folder):

        for file_name in files:
            path = os.path.join(root, file_name)

            try:
                total_size += os.path.getsize(path)
            except OSError:
                pass

    return total_size


def format_size(size):
    units = ["Bytes", "KB", "MB", "GB", "TB"]

    for unit in units:
        if size < 1024:
            return f"{size:.2f} {unit}"

        size /= 1024

    return f"{size:.2f} PB"


def main():
    folder = input("Enter folder path: ").strip()

    if not os.path.isdir(folder):
        print("❌ Folder not found.")
        return

    size = calculate_size(folder)

    print("\n" + "=" * 40)
    print("          📁 FOLDER SIZE")
    print("=" * 40)

    print(f"\nFolder: {folder}")
    print(f"Size  : {format_size(size)}")


if __name__ == "__main__":
    main()