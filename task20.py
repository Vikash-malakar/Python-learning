import os
import json
import base64
import hashlib
from cryptography.fernet import Fernet

VAULT_FILE = "vault.json"


def generate_key(master_password):
    key = hashlib.sha256(master_password.encode()).digest()
    return base64.urlsafe_b64encode(key)


def load_vault():
    if not os.path.exists(VAULT_FILE):
        return []

    try:
        with open(VAULT_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except:
        return []


def save_vault(vault):
    with open(VAULT_FILE, "w", encoding="utf-8") as file:
        json.dump(vault, file, indent=4)


def add_password(vault, fernet):
    website = input("\nWebsite/App: ").strip()
    username = input("Username/Email: ").strip()
    password = input("Password: ").strip()

    if not website or not username or not password:
        print("❌ All fields are required.")
        return

    encrypted_password = fernet.encrypt(
        password.encode()
    ).decode()

    vault.append({
        "website": website,
        "username": username,
        "password": encrypted_password
    })

    save_vault(vault)
    print("✅ Password saved securely!")


def view_passwords(vault, fernet):
    if not vault:
        print("\n❌ No passwords saved.")
        return

    print("\n🔐 SAVED PASSWORDS")
    print("-" * 50)

    for index, item in enumerate(vault, 1):
        try:
            password = fernet.decrypt(
                item["password"].encode()
            ).decode()
        except:
            password = "Unable to decrypt"

        print(f"\n{index}. {item['website']}")
        print(f"   Username: {item['username']}")
        print(f"   Password: {password}")


def main():
    print("\n" + "=" * 50)
    print("             🔐 PASSWORD VAULT")
    print("=" * 50)

    master_password = input("\nEnter master password: ")

    if not master_password:
        print("❌ Master password required.")
        return

    key = generate_key(master_password)
    fernet = Fernet(key)

    vault = load_vault()

    while True:
        print("\n1. Add Password")
        print("2. View Passwords")
        print("3. Exit")

        choice = input("\nChoice: ")

        if choice == "1":
            add_password(vault, fernet)

        elif choice == "2":
            view_passwords(vault, fernet)

        elif choice == "3":
            print("👋 Vault closed.")
            break

        else:
            print("❌ Invalid choice.")


if __name__ == "__main__":
    main()