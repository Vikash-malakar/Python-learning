import os
from PIL import Image

INPUT_FOLDER = "input_images"
OUTPUT_FOLDER = "converted_images"


def convert_images():
    if not os.path.exists(INPUT_FOLDER):
        os.makedirs(INPUT_FOLDER)
        print("📁 input_images folder created.")
        return

    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    target_format = input(
        "Convert images to (png/jpg/webp): "
    ).strip().lower()

    if target_format not in ["png", "jpg", "webp"]:
        print("❌ Invalid format.")
        return

    images = os.listdir(INPUT_FOLDER)

    for file_name in images:
        path = os.path.join(INPUT_FOLDER, file_name)

        try:
            with Image.open(path) as image:

                if target_format == "jpg":
                    if image.mode != "RGB":
                        image = image.convert("RGB")

                name = os.path.splitext(file_name)[0]
                output_path = os.path.join(
                    OUTPUT_FOLDER,
                    f"{name}.{target_format}"
                )

                image.save(output_path)

                print(f"✅ {file_name} → {output_path}")

        except Exception:
            continue

    print("\n🎉 Conversion completed!")


if __name__ == "__main__":
    convert_images()