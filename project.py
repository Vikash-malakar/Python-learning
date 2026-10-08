import os
import shutil


# Folder jisko organize karna hai
FOLDER_PATH = input("Enter folder path: ").strip()


# File extensions ke according categories
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Music": [".mp3", ".wav", ".flac"],
    "Archives": [".zip", ".rar", ".7z"],
    "Programs": [".py", ".java", ".cpp", ".js", ".html", ".css"]
}


def get_category(extension):
    """File extension ke basis par category return karta hai."""

    for category, extensions in FILE_TYPES.items():
        if extension.lower() in extensions:
            return category

    return "Others"


def organize_files():
    if not os.path.exists(FOLDER_PATH):
        print("❌ Folder nahi mila!")
        return

    if not os.path.isdir(FOLDER_PATH):
        print("❌ Ye folder nahi hai!")
        return

    files_moved = 0

    for file_name in os.listdir(FOLDER_PATH):

        file_path = os.path.join(FOLDER_PATH, file_name)

        # Sirf files ko process karo
        if not os.path.isfile(file_path):
            continue

        # File extension
        extension = os.path.splitext(file_name)[1]

        category = get_category(extension)

        # Category folder ka path
        category_path = os.path.join(FOLDER_PATH, category)

        # Folder nahi hai to create karo
        os.makedirs(category_path, exist_ok=True)

        # New file path
        new_path = os.path.join(category_path, file_name)

        # Agar same naam ki file already exist karti hai
        if os.path.exists(new_path):
            name, ext = os.path.splitext(file_name)

            counter = 1

            while os.path.exists(new_path):
                new_file_name = f"{name}_{counter}{ext}"
                new_path = os.path.join(category_path, new_file_name)
                counter += 1

        # File move karo
        shutil.move(file_path, new_path)

        print(f"✅ {file_name} → {category}/")

        files_moved += 1

    print("\n" + "=" * 40)
    print("🎉 ORGANIZATION COMPLETE")
    print("=" * 40)
    print(f"Files moved: {files_moved}")


organize_files()