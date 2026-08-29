import csv
import os


def analyze_csv(file_path):

    if not os.path.exists(file_path):
        print("❌ CSV file not found.")
        return

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            rows = list(reader)

    except Exception as error:
        print(f"❌ Error reading file: {error}")
        return

    if not rows:
        print("❌ CSV file is empty.")
        return

    print("\n" + "=" * 45)
    print("          📊 CSV DATA ANALYZER")
    print("=" * 45)

    print(f"\n📁 File: {file_path}")
    print(f"👥 Total records: {len(rows)}")

    print("\n📌 Columns:")
    for column in rows[0].keys():
        print(f"  • {column}")

    # Marks analysis
    if "Marks" in rows[0]:

        marks = []

        for row in rows:
            try:
                marks.append(float(row["Marks"]))
            except ValueError:
                pass

        if marks:
            average = sum(marks) / len(marks)

            print("\n📈 Marks Analysis")
            print("-" * 30)
            print(f"Highest Marks : {max(marks)}")
            print(f"Lowest Marks  : {min(marks)}")
            print(f"Average Marks : {average:.2f}")

    print("\n👤 Records")
    print("-" * 45)

    for row in rows:
        print(" | ".join(row.values()))

    print("\n" + "=" * 45)


def main():

    file_path = input(
        "Enter CSV file path: "
    ).strip()

    analyze_csv(file_path)


if __name__ == "__main__":
    main()