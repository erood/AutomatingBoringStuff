#! python3
# strong_password_detection.py - tests if a password is strong.

import re
import sys


def main():
    password = input("Enter a password to validate its strongness: ")

    length_regex = re.compile(r"^.{8,}$")
    valid_character_regex = re.compile(r"^[a-zA-Z\d]{8,}$")
    contains_digit_regex = re.compile(r"\d")

    if length_regex.search(password) is None:
        print("Invalid password length.")
        sys.exit(1)

    if valid_character_regex.search(password) is None:
        print("Invalid password characters.")
        sys.exit(2)

    if contains_digit_regex.search(password) is None:
        print("Password should contains at least a digit.")
        sys.exit(3)

    print("Password is strong.")


if __name__ == "__main__":
    main()
