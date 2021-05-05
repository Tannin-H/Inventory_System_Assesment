from tkinter import *
from pickle import dump
from tkinter import messagebox
from tkinter import Canvas


class Item:
    def __init__(self, name, price, qty, vendor):
        self.name = name
        self.price = price
        self.qty = qty
        self.vendor = vendor


class Inventory_GUI:
    def __init__(self, parent):
        self.item_list = [Item("jacket", 12, 5, "warehouse"), Item("Pants", 14, 2, "kmart"), Item("Shirt", 9, 11, "T7"),
                          Item("Shoes", 19, 5, "Nike"), Item("Wakatipu Bucket Hat", 100, 2, "WHS"),
                          Item("jacket", 12, 5, "warehouse"), Item("Pants", 14, 2, "kmart"), Item("Shirt", 9, 11, "T7"),
                          Item("Shoes", 19, 5, "Nike"), Item("Wakatipu Bucket Hat", 100, 2, "WHS"),
                          Item("jacket", 12, 5, "warehouse"), Item("Pants", 14, 2, "kmart"), Item("Shirt", 9, 11, "T7"),
                          Item("Shoes", 19, 5, "Nike"), Item("Wakatipu Bucket Hat", 100, 2, "WHS"),
                          Item("jacket", 12, 5, "warehouse"), Item("Pants", 14, 2, "kmart"), Item("Shirt", 9, 11, "T7"),
                          Item("Shoes", 19, 5, "Nike"), Item("Wakatipu Bucket Hat", 100, 2, "WHS")
                          ]
        self.item_var = IntVar()
        self.items_radbtns = []
        self.price_lbls = []
        self.qty_lbls = []
        self.seller_lbls = []

        sell_btn = Button(parent, text="Sell", command=self.sell_item)
        sell_btn.grid(column=0, row=0, sticky=E + W + N)

        restock_btn = Button(parent, text="Restock", command=self.restock_item)
        restock_btn.grid(column=1, row=0, sticky=E + W + N)

        add_btn = Button(parent, text="Add New Item", command=self.add_item)
        add_btn.grid(column=2, row=0, sticky=E + W + N)

        save_btn = Button(parent, text="Save Inventory", command=self.save_inventory)
        save_btn.grid(column=3, row=0, sticky=E + W + N)

        canvas = Canvas(parent)
        scroll_y = Scrollbar(parent, orient="vertical", command=canvas.yview)

        frame = Frame(canvas)

        # creating the inventory items and packing them into the frame
        product_label = Label(frame, text="Product")
        product_label.grid(column=0, row=0, sticky=W + N)

        price_label = Label(frame, text="Price")
        price_label.grid(column=1, row=0, sticky=W + N)

        quantity_label = Label(frame, text="Qty")
        quantity_label.grid(column=2, row=0, sticky=W + N)

        seller_label = Label(frame, text="Seller")
        seller_label.grid(column=3, row=0, sticky=W + N)

        for item in range(len(self.item_list)):
            self.items_radbtns.append(
                Radiobutton(frame, text=self.item_list[item].name, bg="white", value=item,
                            variable=self.item_var))
            self.items_radbtns[item].grid(column=0, row=item + 1, padx=5, sticky=W + N)

        for item in range(len(self.item_list)):
            self.price_lbls.append(
                Label(frame, text=self.item_list[item].price, bg="white", ))
            self.price_lbls[item].grid(column=1, row=item + 1, padx=5, sticky=W + N)

        for item in range(len(self.item_list)):
            self.qty_lbls.append(
                Label(frame, text=self.item_list[item].qty, bg="white", ))
            self.qty_lbls[item].grid(column=2, row=item + 1, padx=5, sticky=W + N)

        for item in range(len(self.item_list)):
            self.seller_lbls.append(
                Label(frame, text=self.item_list[item].vendor, bg="white", anchor="w"))
            self.seller_lbls[item].grid(column=3, row=item + 1, padx=5, sticky=W + N)

        # put the frame in the canvas
        canvas.create_window(0, 0, anchor='nw', window=frame)
        # make sure everything is displayed before configuring the scrollregion
        canvas.update_idletasks()

        canvas.configure(scrollregion=canvas.bbox('all'),
                         yscrollcommand=scroll_y.set, width=500)

        canvas.grid(column=0, row=2)
        scroll_y.grid(column=1, row=2, sticky=N + S)

        """v_bar = Scrollbar(items_frame)
        v_bar.grid(column=2, row=0)
        canvas = Canvas(items_frame, yscrollcommand=v_bar.set)
        for item in range(len(self.item_list)):
            self.items_radbtns.append(
                Radiobutton(canvas, text=self.item_list[item].name, bg="white", value=item,
                            variable=self.item_var))
            self.items_radbtns[item].grid(column=0, row=item, padx=0, sticky=W + N)
        canvas.grid(column=0, row=0)
        v_bar.config(command=canvas.yview)
"""
        """
        canvas = Canvas(items_frame)
        canvas.create_line(15, 120, 200, 120)
        canvas.grid(column=0, row=0)"""

        """inventory_listbox = Listbox(items_frame, bd=0)
        inventory_listbox.grid(column=0, row=0, sticky=E + W + N)
        inventory_listbox.insert(END, "First Item")
        inventory_listbox.insert(END, "Second Item")
        inventory_listbox.insert(END, "Third Item")"""

    def sell_item(self):
        pass

    def restock_item(self):
        pass

    def add_item(self):
        pass

    def save_inventory(self):
        pass


if __name__ == '__main__':
    root = Tk()
    main_screen = Inventory_GUI(root)
    root.mainloop()
