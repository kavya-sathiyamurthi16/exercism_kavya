"""Functions to keep track and alter inventory."""


def create_inventory(input_list):
    inventory = {}
    for item in input_list:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1
    return inventory


def add_items(inventory, item_list):
    for item in item_list:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1
    return inventory
        


def decrement_items(inventory, items_list):
    for item in items_list:
        if item in inventory and inventory[item] > 0:
            inventory[item] -= 1
    return inventory


def remove_item(inventory, item):
    if item in inventory:
        del inventory[item]
    return inventory


def list_inventory(inventory):
    result = []
    
    for item, quantity in inventory.items():
        if quantity > 0:
            result.append((item, quantity))
    
    return sorted(result)

