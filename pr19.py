import os


def check_keywords():
    file_path = input("Enter resume file path: ").strip()

    if not os.path.exists(file_path):
        print("❌ Resume file not found.")
        return

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            resume = file.read().lower()

    except Exception as error:
        print(f"❌ Error: {error}")
        return

    keywords = input(
        "\nEnter keywords separated by comma:\n"
    ).split(",")

    found = []
    missing = []

    for keyword in keywords:
        keyword = keyword.strip().lower()

        if not keyword:
            continue

        if keyword in resume:
            found.append(keyword)
        else:
            missing.append(keyword)

    total = len(found) + len(missing)

    print("\n" + "=" * 50)
    print("          📄 RESUME KEYWORD CHECKER")
    print("=" * 50)

    print("\n✅ Found Keywords:")
    for keyword in found:
        print(f"  ✔ {keyword}")

    print("\n❌ Missing Keywords:")
    for keyword in missing:
        print(f"  ✘ {keyword}")

    if total:
        score = (len(found) / total) * 100
        print(f"\n📊 Keyword Match: {score:.2f}%")

    print("=" * 50)


if __name__ == "__main__":
    check_keywords()