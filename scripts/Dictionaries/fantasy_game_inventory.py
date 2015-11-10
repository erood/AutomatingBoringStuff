#! python3
# fantasy_game_inventory.py -  takes a dictionary and prints its contents in value key format
__author__ = 'm'


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
