__author__ = 'm'

"""
You are creating a fantasy video game. The data structure to model the
player's inventory will be a dictionary where the keys are string values
describing the item in the inventory and the value is an integer value detailing
how many of that item the player has. For example, the dictionary value
{'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} means the
player has 1 rope, 6 torches, 42 gold coins, and so on
"""


def display_inventory(inventory):
    total_number_of_items = 0
    for item, quantity in inventory.items():
        print(quantity, item)
        total_number_of_items += quantity
    print("Total number of items: " + str(total_number_of_items))


def main():
    stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
    display_inventory(stuff)


if __name__ == "__main__":
    main()
