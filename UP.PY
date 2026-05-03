import random
import string

print("=== Simple URL Shortener ===")

FILE_NAME = "urls.txt"

def generate_code(length=6):
    chars = string.ascii_letters + string.digits
    code = ""
    for _ in range(length):
        code += random.choice(chars)
    return code

def shorten_url():
    long_url = input("Enter long URL: ")

    code = generate_code()

    with open(FILE_NAME, "a") as file:
        file.write(code + "," + long_url + "\n")

    print("Short Code:", code)

def get_url():
    code = input("Enter short code: ")

    try:
        with open(FILE_NAME, "r") as file:
            data = file.readlines()

            for line in data:
                c, url = line.strip().split(",", 1)
                if c == code:
                    print("Original URL:", url)
                    return

            print("Code not found")

    except FileNotFoundError:
        print("No data found")

while True:
    print("\n1. Shorten URL")
    print("2. Get Original URL")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        shorten_url()

    elif choice == "2":
        get_url()

    elif choice == "3":
        print("Program Closed")
        break

    else:
        print("Invalid Choice")