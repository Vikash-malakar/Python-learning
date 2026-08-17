import qrcode
import os


OUTPUT_FOLDER = "generated_qr"


def generate_qr():
    print("\n" + "=" * 40)
    print("        🔲 QR CODE GENERATOR")
    print("=" * 40)

    data = input("\nEnter text or URL: ").strip()

    if not data:
        print("❌ Text or URL cannot be empty.")
        return

    file_name = input("Enter file name: ").strip()

    if not file_name:
        file_name = "my_qr"

    # Create output folder
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    # Add extension
    if not file_name.lower().endswith(".png"):
        file_name += ".png"

    output_path = os.path.join(OUTPUT_FOLDER, file_name)

    # Create QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4
    )

    qr.add_data(data)
    qr.make(fit=True)

    # Generate image
    image = qr.make_image()

    # Save image
    image.save(output_path)

    print("\n✅ QR Code generated successfully!")
    print(f"📁 Saved at: {output_path}")


if __name__ == "__main__":
    generate_qr()