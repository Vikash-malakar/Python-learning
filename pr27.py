import os
from PIL import Image


def show_metadata():
    file_path = input(
        "Enter image path: "
    ).strip()

    if not os.path.exists(file_path):
        print("❌ Image not found.")
        return

    try:
        with Image.open(file_path) as image:

            file_size = os.path.getsize(file_path)
            file_size_kb = file_size / 1024

            print("\n" + "=" * 50)
            print("          🖼️ IMAGE METADATA")
            print("=" * 50)

            print(f"\n📁 File       : {file_path}")
            print(f"📐 Width      : {image.width}px")
            print(f"📐 Height     : {image.height}px")
            print(f"📊 Format     : {image.format}")
            print(f"🎨 Mode       : {image.mode}")
            print(f"💾 File Size  : {file_size_kb:.2f} KB")

            print("\n" + "=" * 50)

    except Exception as error:
        print(f"❌ Error: {error}")


if __name__ == "__main__":
    show_metadata()