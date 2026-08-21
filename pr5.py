from collections import Counter
import re
import os


def analyze_file(file_path):
    if not os.path.exists(file_path):
        print("❌ File nahi mili.")
        return

    if not file_path.lower().endswith(".txt"):
        print("❌ Sirf .txt files supported hain.")
        return

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()

    except UnicodeDecodeError:
        print("❌ File encoding read nahi ho saki.")
        return

    except PermissionError:
        print("❌ File access permission denied.")
        return

    # Lines
    lines = text.splitlines()

    # Words
    words = re.findall(r"\b[a-zA-Z0-9']+\b", text.lower())

    # Characters
    characters = len(text)

    # Characters without spaces
    characters_without_spaces = len(
        text.replace(" ", "").replace("\n", "").replace("\t", "")
    )

    # Word frequency
    word_frequency = Counter(words)

    print("\n" + "=" * 50)
    print("           📊 TEXT FILE ANALYZER")
    print("=" * 50)

    print(f"\n📄 File: {file_path}")
    print(f"📑 Lines: {len(lines)}")
    print(f"🔤 Words: {len(words)}")
    print(f"🔡 Characters: {characters}")
    print(f"🔡 Characters (without spaces): {characters_without_spaces}")

    print("\n🔥 Top 10 Most Used Words")
    print("-" * 30)

    for word, count in word_frequency.most_common(10):
        print(f"{word:<20} {count}")

    print("\n" + "=" * 50)


def main():
    print("📊 Text File Analyzer")

    file_path = input("\nEnter .txt file path: ").strip()

    analyze_file(file_path)


if __name__ == "__main__":
    main()