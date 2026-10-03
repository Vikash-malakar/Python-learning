import csv
import json
import os


def convert_csv_to_json():
    input_file = "input.csv"
    output_file = "output.json"

    if not os.path.exists(input_file):
        print("❌ input.csv not found.")
        return

    try:
        with open(input_file, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            data = list(reader)

        with open(output_file, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        print("\n✅ CSV converted to JSON!")
        print(f"📁 Output: {output_file}")
        print(f"📊 Records: {len(data)}")

    except Exception as error:
        print(f"❌ Error: {error}")


if __name__ == "__main__":
    convert_csv_to_json()