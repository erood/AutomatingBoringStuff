#! python3
# fantasy_game_inventory.py -  contains functions to add a list of items to a dictionary and print it.
__author__ = 'm'


def display_inventory(inventory):
    total_number_of_items = 0

    for item, quantity in inventory.items():
        print(quantity, item)
        total_number_of_items += quantity

    print("Total number of items: " + str(total_number_of_items))


def add_to_inventory(inventory, items_to_add):
    for item in items_to_add:
        inventory[item] = inventory.get(item, 0) + 1


def main():
    inventory = {'gold coin': 42, 'rope': 1}
    dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
    add_to_inventory(inventory, dragon_loot)
    display_inventory(inventory)


if __name__ == "__main__":
    main()
