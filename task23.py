import markdown
import os


def convert_markdown():
    input_file = "input.md"
    output_file = "output.html"

    if not os.path.exists(input_file):
        print("❌ input.md not found.")
        return

    try:
        with open(input_file, "r", encoding="utf-8") as file:
            markdown_text = file.read()

        html = markdown.markdown(
            markdown_text,
            extensions=["tables", "fenced_code"]
        )

        full_html = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Markdown Document</title>
</head>
<body>

{html}

</body>
</html>
"""

        with open(output_file, "w", encoding="utf-8") as file:
            file.write(full_html)

        print("\n✅ Markdown converted to HTML!")
        print(f"📁 Output: {output_file}")

    except Exception as error:
        print(f"❌ Error: {error}")


if __name__ == "__main__":
    convert_markdown()