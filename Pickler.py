import pickle


class Item:
    def __init__(self, name, price, qty, vendor):
        self.name = name
        self.price = price
        self.qty = qty
        self.vendor = vendor


file = open("inventory_database", "wb")

inventory_items = [Item("Jacket", 12.0, 5, "Warehouse"), Item("Pants", 14.0, 2, "Kmart"), Item("Shirt", 9.0, 11, "T7"),
                   Item("Shoes", 19.0, 5, "Nike"), Item("Wakatipu Bucket Hat", 100.0, 2, "WHS"),
                   Item("Shorts", 20.0, 7, "Kmart")]

pickle.dump(inventory_items, file)
file.close()
