print("=== Password Strength Checker ===")

password = input("Enter your password: ")

length = len(password)

has_digit = False
has_upper = False

for ch in password:
    if ch.isdigit():
        has_digit = True
    if ch.isupper():
        has_upper = True

# Logic
if length >= 8 and has_digit and has_upper:
    print(" Strong Password")
elif length >= 6:
    print(" Medium Password")
else:
    print(" Weak Password")