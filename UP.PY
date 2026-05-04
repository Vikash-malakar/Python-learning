import os
import shutil

print("=== File Organizer ===")

path = input("Enter folder path: ")

if not os.path.exists(path):
    print("Invalid Path")
else:
    files = os.listdir(path)

    for file in files:
        file_path = os.path.join(path, file)

        if os.path.isfile(file_path):
            ext = file.split(".")[-1]

            folder_path = os.path.join(path, ext)

            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            shutil.move(file_path, os.path.join(folder_path, file))

    print("Files Organized Successfully")