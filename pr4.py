import os
import hashlib


FOLDER_PATH = input("Enter folder path: ").strip()


def calculate_hash(file_path):
    """File ka unique hash calculate karta hai."""

    hash_object = hashlib.md5()

    try:
        with open(file_path, "rb") as file:
            while True:
                data = file.read(4096)

                if not data:
                    break

                hash_object.update(data)

        return hash_object.hexdigest()

    except (PermissionError, OSError):
        return None


def find_duplicates(folder_path):

    if not os.path.exists(folder_path):
        print("❌ Folder nahi mila.")
        return

    if not os.path.isdir(folder_path):
        print("❌ Ye ek folder nahi hai.")
        return

    file_hashes = {}
    duplicate_groups = []

    print("\n🔍 Searching for duplicate files...\n")

    for root, directories, files in os.walk(folder_path):

        for file_name in files:

            file_path = os.path.join(root, file_name)

            file_hash = calculate_hash(file_path)

            if file_hash is None:
                continue

            if file_hash in file_hashes:

                # Existing duplicate group
                found = False

                for group in duplicate_groups:
                    if file_hash in group["hash"]:
                        group["files"].append(file_path)
                        found = True
                        break

                if not found:
                    duplicate_groups.append({
                        "hash": file_hash,
                        "files": [
                            file_hashes[file_hash],
                            file_path
                        ]
                    })

            else:
                file_hashes[file_hash] = file_path

    if not duplicate_groups:
        print("✅ No duplicate files found.")
        return

    print("=" * 60)
    print("             🔍 DUPLICATE FILES")
    print("=" * 60)

    duplicate_count = 0

    for number, group in enumerate(duplicate_groups, start=1):

        print(f"\nGroup {number}:")

        for file_path in group["files"]:
            print(f"  📄 {file_path}")

        duplicate_count += len(group["files"]) - 1

    print("\n" + "=" * 60)
    print(f"Total duplicate files: {duplicate_count}")
    print("=" * 60)


find_duplicates(FOLDER_PATH)