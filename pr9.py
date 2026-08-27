import os
import shutil
from datetime import datetime


def create_backup():
    source = input("Enter folder path to backup: ").strip()

    if not os.path.exists(source):
        print("❌ Folder not found.")
        return

    if not os.path.isdir(source):
        print("❌ Please enter a folder path.")
        return

    folder_name = os.path.basename(os.path.abspath(source))

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    backup_folder = "backups"
    os.makedirs(backup_folder, exist_ok=True)

    backup_name = f"{folder_name}_backup_{timestamp}"

    destination = os.path.join(
        backup_folder,
        backup_name
    )

    try:
        shutil.copytree(source, destination)

        print("\n✅ Backup created successfully!")
        print(f"📁 Backup location: {destination}")

    except OSError as error:
        print(f"❌ Backup failed: {error}")


if __name__ == "__main__":
    print("\n" + "=" * 45)
    print("          💾 FILE BACKUP TOOL")
    print("=" * 45)

    create_backup()