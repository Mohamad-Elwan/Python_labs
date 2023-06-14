import random
import string

def generate_password(length=8, include_digits=True, include_symbols=True):
    characters = string.ascii_letters
    if include_digits:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def get_password_length():
    while True:
        try:
            length = int(input("Enter the desired password length: "))
            if length <= 0:
                print("Length should be a positive integer.")
            else:
                return length
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def get_yes_or_no(prompt):
    while True:
        response = input(prompt).strip().lower()
        if response in ['yes', 'y']:
            return True
        elif response in ['no', 'n']:
            return False
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

password_length = get_password_length()
include_digits = get_yes_or_no("Include digits? (yes/no): ")
include_symbols = get_yes_or_no("Include symbols? (yes/no): ")

password = generate_password(password_length, include_digits, include_symbols)
print("Generated Password:", password)
