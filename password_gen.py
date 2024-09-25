#random password generator

import random
import string

def generate_password(length, uppercase, lowercase, numbers, symbols):
    password_char = ''
    if uppercase:
        password_char += string.ascii_uppercase
    if lowercase:
        password_char += string.ascii_lowercase
    if numbers:
        password_char += string.digits
    if symbols:
        password_char += string.punctuation

    if length < 8:
        print("Password length should be at least 8 characters.")
        return None

    password = ''.join(random.choice(password_char) for i in range(length))
    return password

def main():
    print("Password Generator")

    length = int(input("Enter password length (at least 8 characters): "))

    uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    numbers = input("Include numbers? (y/n): ").lower() == 'y'
    symbols = input("Include symbols? (y/n): ").lower() == 'y'

    password = generate_password(length, uppercase, lowercase, numbers, symbols)

    if password:
        print("Generated password: ", password)

if __name__ == "__main__":
    main()