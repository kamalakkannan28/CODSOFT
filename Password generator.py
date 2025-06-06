import random

print("--- PASSWORD GENERATOR ---")
length = int(input("Enter password length: "))

password = ""
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"

for i in range(length):
    password = password + random.choice(characters)

print("Generated Password:", password)
