#from PP2FGI import displayInventory

def addToInventory(inventory, addedItems):
    for i in range(len(addedItems)):
        if addedItems[i] in inventory:
             inventory[addedItems[i]] += 1
        else:
            inventory[str(addedItems[i])] = 1
    return inventory

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
#dragonLoot = ['gold coin', 'rope', 'gold coin', 'gold coin']
inv = addToInventory(inv, dragonLoot)

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        # FILL THIS PART IN
        print(str(v) + ' ' + str(k))
        item_total += v
    print("Total number of items: " + str(item_total))

displayInventory(inv)