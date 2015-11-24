#! python3
# strip_regex.py - takes a string and uses a regular expression to do the same as the strip function.

import re


def strip_regex(string_to_strip, to_strip=r"\s"):
    initial_strip_regex = re.compile(r"^(" + to_strip + ")*")
    final_strip_regex = re.compile(r"(" + to_strip + ")*$")

    stripped_string = final_strip_regex.sub("", initial_strip_regex.sub("", string_to_strip))

    return stripped_string


def main():
    string_to_strip = input("Enter a string to be striped: ")
    to_strip = input("Enter a string to strip: ")

    print(strip_regex(string_to_strip, to_strip))
    string_to_strip = input("Enter a string to be striped with whitespaces at the beggining and at the end: ")
    print(strip_regex(string_to_strip))


if __name__ == "__main__":
    main()
