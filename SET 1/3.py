import random
import string
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(characters, k=length))
    return password
try:
    length = int(input("Enter the desired password length: "))
    password = generate_password(length)
    print(f"Generated password: {password}")
except ValueError:
    print("Please enter a valid number for the password length.")
