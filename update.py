import random

print("=== Password Generator ===")

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890@#$%&*"

length = int(input("Enter password length: "))

password = ""

for i in range(length):
    password += random.choice(chars)

print("Generated Password:", password)