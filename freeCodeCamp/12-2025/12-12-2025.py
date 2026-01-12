def find_in_shipment(shipment, toFind):
    for i in range(len(shipment)):
        if shipment[i][1] == toFind:
            return i
    return None

def update_inventory(inventory, shipment):

    
    for i in inventory:
        fund = find_in_shipment(shipment, i[1])

        if fund != None:
            product = shipment.pop(fund)

            i[0] = i[0] + product[0]
    
    if len(shipment) > 0:
        inventory.extend(shipment)

    return inventory

print(update_inventory([[2, "apples"], [5, "bananas"]], [[1, "apples"], [3, "bananas"]]))
print(update_inventory([[2, "apples"], [5, "bananas"]], [[1, "apples"], [3, "bananas"], [4, "oranges"]]))
print(update_inventory([], [[10, "apples"], [30, "bananas"], [20, "oranges"]]))
print(update_inventory([[0, "Bowling Ball"], [0, "Dirty Socks"], [0, "Hair Pin"], [0, "Microphone"]], [[1, "Hair Pin"], [1, "Half-Eaten Apple"], [1, "Bowling Ball"], [1, "Toothpaste"]]))
