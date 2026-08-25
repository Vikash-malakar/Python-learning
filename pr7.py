import os
from PIL import Image


INPUT_FOLDER = "input_images"
OUTPUT_FOLDER = "resized_images"

SUPPORTED_FORMATS = (
    ".jpg",
    ".jpeg",
    ".png",
    ".webp"
)


def resize_images(width, height):

    # Input folder check
    if not os.path.exists(INPUT_FOLDER):
        os.makedirs(INPUT_FOLDER)

        print(f"📁 '{INPUT_FOLDER}' folder create ho gaya.")
        print("Is folder me images daalo aur program dobara run karo.")
        return

    # Output folder create
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    images = [
        file
        for file in os.listdir(INPUT_FOLDER)
        if file.lower().endswith(SUPPORTED_FORMATS)
    ]

    if not images:
        print("❌ Input folder me koi image nahi mili.")
        return

    print("\n" + "=" * 50)
    print("           🖼️ IMAGE RESIZER")
    print("=" * 50)

    print(f"\n📸 Images found: {len(images)}")
    print(f"📐 New size: {width} x {height}\n")

    successful = 0

    for file_name in images:

        input_path = os.path.join(
            INPUT_FOLDER,
            file_name
        )

        output_path = os.path.join(
            OUTPUT_FOLDER,
            file_name
        )

        try:
            with Image.open(input_path) as image:

                original_size = image.size

                resized_image = image.resize(
                    (width, height)
                )

                # JPEG ke liye RGB conversion
                if file_name.lower().endswith(
                    (".jpg", ".jpeg")
                ):
                    if resized_image.mode != "RGB":
                        resized_image = resized_image.convert("RGB")

                resized_image.save(output_path)

                print(
                    f"✅ {file_name} "
                    f"{original_size} → "
                    f"{width}x{height}"
                )

                successful += 1

        except Exception as error:
            print(f"❌ {file_name}: {error}")

    print("\n" + "=" * 50)
    print("       🎉 RESIZING COMPLETE")
    print("=" * 50)

    print(f"\n✅ Successfully resized: {successful}")
    print(f"📁 Saved in: {OUTPUT_FOLDER}/")


def main():

    print("\n🖼️ Python Image Resizer")

    try:
        width = int(input("Enter new width: "))
        height = int(input("Enter new height: "))

        if width <= 0 or height <= 0:
            print("❌ Width and height must be greater than 0.")
            return

    except ValueError:
        print("❌ Please enter valid numbers.")
        return

    resize_images(width, height)


if __name__ == "__main__":
    main()