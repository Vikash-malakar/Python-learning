import tkinter as tk


def analyze_text():
    text = text_box.get("1.0", tk.END).strip()

    words = len(text.split())
    characters = len(text)
    characters_no_spaces = len(text.replace(" ", ""))
    lines = len(text.splitlines())

    result.config(
        text=(
            f"Words: {words}\n"
            f"Characters: {characters}\n"
            f"Characters without spaces: {characters_no_spaces}\n"
            f"Lines: {lines}"
        )
    )


def clear_text():
    text_box.delete("1.0", tk.END)
    result.config(text="")


root = tk.Tk()

root.title("Word Counter")
root.geometry("600x450")

title = tk.Label(
    root,
    text="📝 Word Counter",
    font=("Arial", 24, "bold")
)

title.pack(pady=15)

text_box = tk.Text(
    root,
    height=12,
    width=60,
    font=("Arial", 12)
)

text_box.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

analyze_button = tk.Button(
    button_frame,
    text="Analyze",
    command=analyze_text,
    width=15
)

analyze_button.pack(side=tk.LEFT, padx=5)

clear_button = tk.Button(
    button_frame,
    text="Clear",
    command=clear_text,
    width=15
)

clear_button.pack(side=tk.LEFT, padx=5)

result = tk.Label(
    root,
    text="",
    font=("Arial", 12),
    justify=tk.LEFT
)

result.pack(pady=15)

root.mainloop()