import os
from pypdf import PdfWriter


INPUT_FOLDER = "input_pdfs"
OUTPUT_FOLDER = "output"


def merge_pdfs():
    print("\n" + "=" * 45)
    print("          📄 PDF MERGER")
    print("=" * 45)

    # Check input folder
    if not os.path.exists(INPUT_FOLDER):
        os.makedirs(INPUT_FOLDER)
        print(f"\n📁 '{INPUT_FOLDER}' folder create ho gaya.")
        print("Is folder me PDF files daalo aur program dobara run karo.")
        return

    # Get PDF files
    pdf_files = [
        file for file in os.listdir(INPUT_FOLDER)
        if file.lower().endswith(".pdf")
    ]

    if not pdf_files:
        print("\n❌ input_pdfs folder me koi PDF nahi hai.")
        return

    # Sort files alphabetically
    pdf_files.sort()

    print(f"\n📚 {len(pdf_files)} PDF files found.")

    # Create output folder
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    writer = PdfWriter()

    # Add each PDF
    for pdf_file in pdf_files:
        file_path = os.path.join(INPUT_FOLDER, pdf_file)

        print(f"➕ Adding: {pdf_file}")

        writer.append(file_path)

    # Output file
    output_path = os.path.join(
        OUTPUT_FOLDER,
        "merged_document.pdf"
    )

    # Save merged PDF
    with open(output_path, "wb") as output_file:
        writer.write(output_file)

    writer.close()

    print("\n" + "=" * 45)
    print("       ✅ PDF MERGED SUCCESSFULLY")
    print("=" * 45)

    print(f"\n📄 Output: {output_path}")


if __name__ == "__main__":
    merge_pdfs()