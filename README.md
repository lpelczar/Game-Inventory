# Game Inventory

## Story

You are creating a fantasy video game. The data structure to model the player’s inventory will be a dictionary where the keys are string values describing the item in the inventory and the value is an integer value detailing how many of that item the player has. For example, the dictionary value
```
inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} 
```
means the player has 1 rope, 6 torches, 42 gold coins, and so on.

Write a function named display_inventory(inventory) that would take any possible “inventory” and display it like the following:

Inventory:
- 12 arrow
- 42 gold coin
- 1 rope
- 6 torch
- 1 dagger
Total number of items: 62
Hint: You can use a for loop to loop through all the keys in a dictionary.

Imagine that a vanquished dragon’s loot is represented as a list of strings like this:
```
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
```
Write a function named add_to_inventory(inventory, added_items), where the inventory parameter is a dictionary representing the player’s inventory and the added_items parameter is a list like dragon_loot. The add_to_inventory() function should return a dictionary that represents the updated inventory. Note that the added_items list can contain multiples of the same item. Your code could look something like this:

def add_to_inventory(inventory, added_items):
your code goes here

dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = add_to_inventory(inv, dragon_loot)
display_inventory(inv)
The display_inventory() function (from the previous step) should output the following:

Inventory:
- 12 arrow
- 45 gold coin
- 1 rope
- 1 ruby
- 6 torch
- 2 dagger
Total number of items: 67

Write a function named print_table(inventory, order) that takes your inventory and displays it in a well-organized table with each column right-justified. The input argument is an order parameter (string), which works as the following:
- empty (by default) means the table is unordered
- "count,desc" means the table is ordered by count (of items in the inventory) in descending order
- "count,asc" means the table is ordered by count in ascending order

Based on the previous inventory values, your print_table(inventory, "count,desc") function would print the following:

Inventory:
  count    item name
--------------------
     45    gold coin
     12        arrow
      6        torch
      2       dagger
      1         rope
      1         ruby
--------------------
Total number of items: 67
Hint: Your code will first have to find the longest string in each of the inner lists so that the whole column can be wide enough to fit all the strings.

Write a function named import_inventory(inventory, filename) which can import new inventory items from a file - the filename comes as an argument, but by default it's "import_inventory.csv". The import automatically merges items by name. The file format is plain text with comma separated values (CSV). Example file content:

ruby,rope,ruby,gold coin,ruby,axe
After importing a file like this, the print_table function should output the following:

Inventory:
  count    item name
--------------------
     46    gold coin
     12        arrow
      6        torch
      4         ruby
      2         rope
      2       dagger
      1          axe
--------------------
Total number of items: 73
Be aware, that it merged the ruby and rope items by name, and didn't duplicate it.

Write a function named export_inventory(inventory, filename) which can export all inventory items to a file. The filename comes as an argument - if not, it automatically creates (and overwrites) the file called "export_inventory.csv". The file format is the same plain text with comma separated values (CSV).

Ensure your functions are working with specially named items, which have a unicode character or accent in their name or other special characters (especially space, tab).

## More info

Project made for [Codecool](https://codecool.com/) programming course.
