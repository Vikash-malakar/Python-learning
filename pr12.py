import os


OUTPUT_FOLDER = "contacts"


def create_contact():

    print("\n" + "=" * 45)
    print("        📇 CONTACT CARD GENERATOR")
    print("=" * 45)

    name = input("\nEnter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()
    organization = input("Enter organization: ").strip()

    if not name or not phone:
        print("\n❌ Name and phone are required.")
        return

    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    file_name = name.replace(" ", "_") + ".vcf"

    file_path = os.path.join(
        OUTPUT_FOLDER,
        file_name
    )

    contact_data = f"""BEGIN:VCARD
VERSION:3.0
FN:{name}
TEL:{phone}
EMAIL:{email}
ORG:{organization}
END:VCARD
"""

    try:
        with open(
            file_path,
            "w",
            encoding="utf-8"
        ) as file:

            file.write(contact_data)

        print("\n✅ Contact card created!")
        print(f"📁 Saved at: {file_path}")

    except OSError as error:
        print(f"\n❌ Error: {error}")


if __name__ == "__main__":
    create_contact()