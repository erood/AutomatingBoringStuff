#! python3
__author__ = 'm'

"""
Imagine that a vanquished dragon's loot is represented as a list of strings
like this:
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
Write a function named addToInventory(inventory, addedItems), where the
inventory parameter is a dictionary representing the player's inventory (like
in the previous project) and the addedItems parameter is a list like dragonLoot.
"""

from fantasy_game_inventory import display_inventory


def add_to_inventory(inventory, items_to_add):
    for item in items_to_add:
        inventory[item] = inventory.get(item, 0) + 1


def main():
    inventory = {'gold coin': 42, 'rope': 1}
    dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
    add_to_inventory(inventory, dragon_loot)
    display_inventory(inventory)


if __name__ == "__main__":
    # main()

    print("""This is a goodbye
and is not the end of the world
    because I am going to change it.
    """)