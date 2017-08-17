import operator
# This is the file where you must work. Write code in the functions, create new functions,
# so they work according to the specification


def display_inventory(inventory):
    """Display the inventory.

    Args:
        inventory(dict): our inventory
    """
    print("Inventory:")
    total = 0
    for k, v in inventory.items():
        print("%d %s" % (v, k))
        total += v
    print("Total number of items: %d" % total)


def add_to_inventory(inventory, added_items):
    """Adds to the inventory dictionary a list of items from added_items.

    Args:
        inventory(dict): our inventory
        added_items(list): list of items which we want to add to our inventory

    Returns:
        inventory(dict): inventory with added items
    """
    for i in added_items:
        if i in inventory.keys():
            inventory[i] += 1
        else:
            inventory[i] = 1
    return inventory


def remove_from_inventory(inventory, removed_items):
    """Removes from the inventory dictionary a list of items from removed_items.

    Args:
        inventory(dict): our inventory
        removed_items(list): list of items which we want to remove from our inventory
    Returns:
        inventory(dict): our inventory with removed items
    """
    for i in removed_items:
        if i in inventory.keys():
            if inventory[i] > 1:
                inventory[i] -= 1
            else:
                del inventory[i]
    return inventory


def change_item_name(inventory, old_name, new_name):
    """Change one old item name to a new name in our inventory

    Args:
        inventory(dict): our inventory
        old_name(string): current name of the item
        new_name(string): new name of the item
    Returns:
        inventory(dict): our inventory with changed item name
    """
    for k, v in inventory.items():
        if k == old_name:
            inventory[new_name] = inventory.pop(old_name)
    return inventory


def set_item_value(inventory, item_name, new_value):
    """Change one old item name to a new name in our inventory

    Args:
        inventory(dict): our inventory
        item_name(string): name of the item which value we want to change
        new_value(int): new value of the item
    Returns:
        inventory(dict): our inventory with changed item value
    """
    for k, v in inventory.items():
        if k == item_name:
            inventory[item_name] = new_value
    return inventory


def print_table(inventory, order=None):
    """Takes your inventory and displays it in a well-organized table with each column right-justified.

        Args:
            inventory(dict): our inventory

        Keyword args:
            order(string):
                - None (by default) means the table is unordered
                - "count,desc" means the table is ordered by count (of items in the inventory) in descending order
                - "count,asc" means the table is ordered by count in ascending order
        """
    label_1 = 'count'
    label_2 = 'item name'
    # Spacing between each column in table
    spacing = 3
    values_spacing = 4
    # Find the longest string in each column of the table so the column can be wide enough to fit all the values.
    max_key_length = max(max(len(x) for x in inventory), len(label_1))
    max_value_length = max(max(len(str(x)) for x in inventory.values()), len(label_2))

    # Sort the inventory depending on which order parameter is passed to function
    if order == 'count,asc':
        sorted_inventory = sorted(inventory.items(), key=operator.itemgetter(1))
    elif order == 'count,desc':
        sorted_inventory = sorted(inventory.items(), key=operator.itemgetter(1), reverse=True)
    elif order is None:
        sorted_inventory = inventory.items()
    else:
        raise ValueError("Wrong order argument!")

    # Print the table using rjust - a build-in function which right justifies the values.
    print('Inventory:')
    print(label_1.rjust(max_value_length), label_2.rjust(max_key_length + spacing))
    print('-' * (max_key_length + max_value_length + values_spacing))
    for k, v in sorted_inventory:
        print(repr(v).rjust(max_value_length), k.rjust(max_key_length + spacing))
    print('-' * (max_key_length + max_value_length + values_spacing))
    print('Total number of items: %d' % sum(inventory.values()))


def import_inventory(inventory, filename="import_inventory.csv"):
    """Imports new inventory items from a file. The filename comes as an argument, but by default it's
        "import_inventory.csv". The import automatically merges items by name.
        The file format is plain text with comma separated values (CSV).

    Args:
        inventory(dict): our inventory
        filename(csv file): file with comma separated values from which we are importing values
    Returns:
        inventory(dict): our inventory with changed item value
    """
    with open(filename) as f:
        read_data = f.read()
    imported_data = read_data.split(',')
    for i in imported_data:
        if i in inventory.keys():
            inventory[i] += 1
        else:
            inventory[i] = 1
    print_table(inventory, order='count,desc')
    return inventory


def export_inventory(inventory, filename="export_inventory.csv"):
    """Exports the inventory into a .csv file. If the filename argument is None it creates and overwrites a file
        called "export_inventory.csv". The file format is the same plain text with comma separated values (CSV).

    Args:
        inventory(dict): our inventory
        filename(csv file): file with comma separated values to which we are exporting values
    """
    list = []
    for k, v in inventory.items():
        for i in range(0, v):
            list.append(k)
    with open(filename, 'w') as f:
        f.write(",".join(list))


def main():
    """
    Main function tests all the other functions
    """
    inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
    print_table(inv)
    dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
    inv = add_to_inventory(inv, dragon_loot)
    display_inventory(inv)
    print_table(inv, order='count,desc')
    inv = remove_from_inventory(inv, dragon_loot)
    print_table(inv, order='count,asc')
    inv = change_item_name(inv, 'gold coin', 'red coin')
    print_table(inv, order='count,desc')
    inv = set_item_value(inv, 'red coin', 200)
    print_table(inv, order='count,desc')
    inv = {}
    import_inventory(inv, 'test_inventory.csv')
    print_table(inv, order='count,asc')
    export_inventory(inv)


if __name__ == "__main__":
    main()
