import os
import re

INPUT_FILE = "input.txt"
OUTPUT_FOLDER = "output"


def clean_text(text):
    cleaned_lines = []

    for line in text.splitlines():
        # Extra spaces and tabs remove
        line = re.sub(r"[ \t]+", " ", line).strip()

        # Empty lines ignore
        if line:
            cleaned_lines.append(line)

    return "\n".join(cleaned_lines)


def main():
    print("\n" + "=" * 50)
    print("            🧹 TEXT CLEANER TOOL")
    print("=" * 50)

    if not os.path.exists(INPUT_FILE):
        print(f"\n❌ '{INPUT_FILE}' file nahi mili.")
        return

    try:
        with open(INPUT_FILE, "r", encoding="utf-8") as file:
            original_text = file.read()

    except UnicodeDecodeError:
        print("\n❌ File encoding support nahi karti.")
        return

    except OSError as error:
        print(f"\n❌ File read error: {error}")
        return

    cleaned_text = clean_text(original_text)

    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    output_file = os.path.join(
        OUTPUT_FOLDER,
        "cleaned_text.txt"
    )

    try:
        with open(output_file, "w", encoding="utf-8") as file:
            file.write(cleaned_text)

    except OSError as error:
        print(f"\n❌ File save error: {error}")
        return

    print("\n✅ Text cleaned successfully!")

    print("\n📊 File Statistics")
    print("-" * 35)
    print(f"Original characters : {len(original_text)}")
    print(f"Cleaned characters  : {len(cleaned_text)}")
    print(f"Original lines      : {len(original_text.splitlines())}")
    print(f"Cleaned lines       : {len(cleaned_text.splitlines())}")

    print("\n📁 Output file:")
    print(output_file)

    print("\n" + "=" * 50)


if __name__ == "__main__":
    main()