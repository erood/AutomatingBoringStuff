__author__ = 'm'

"""
Write a function that takes a list value as an argument and returns
a string with all the items separated by a comma and a space, with and
inserted before the last item.
"""


def separate_items_by_commas(items):
    separated_items_by_commas = ""

    for item in items[:-1]:
        separated_items_by_commas += item + ", "

    return separated_items_by_commas + "and " + items[-1]


def main():
    spam = ["apples", "bananas", "tofu", "cats", "dogs"]
    print(separate_items_by_commas(spam))


if __name__ == "__main__":
    main()
