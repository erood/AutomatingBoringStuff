#! python3
__author__ = 'm'

"""
Write a function named collatz() that has one parameter named number. If
number is even, then collatz() should print number // 2 and return this value.
If number is odd, then collatz() should print and return 3 * number + 1.
Then write a program that lets the user type in an integer and that keeps
calling collatz() on that number until the function returns the value 1.
"""

import sys

def generate_next_collatz_number(number):
    if number % 2 == 0:
        return number // 2
    return 3 * number + 1


def generate_collatz_sequence(number):
    sequence = [generate_next_collatz_number(number)]
    while sequence[-1] != 1:
        sequence.append(generate_next_collatz_number(sequence[-1]))
    return sequence


def main():
    try:
        number = int(input("Enter an integer number:\n"))
    except ValueError:
        print("The data entered was not an integer.")
        sys.exit(-1)

    for generated_number in generate_collatz_sequence(number):
        print(generated_number)


if __name__ == "__main__":
    main()
