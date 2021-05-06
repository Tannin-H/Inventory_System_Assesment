from tkinter import *
from pickle import dump
from tkinter import messagebox
from tkinter import simpledialog
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
                          Item("Shoes", 19, 5, "Nike"), Item("Wakatipu Bucket Hat", 100, 2, "WHS")]
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

        self.canvas = Canvas(parent)
        self.scroll_y = Scrollbar(parent, orient="vertical", command=self.canvas.yview)

        self.frame = Frame(self.canvas, bg="white")

        # creating the inventory items and packing them into the frame
        product_label = Label(self.frame, text="Product", bg="white", font=("Helvetica Neue", 15))
        product_label.grid(column=0, row=0, sticky=W + N)

        price_label = Label(self.frame, text="Price", bg="white", font=("Helvetica Neue", 15))
        price_label.grid(column=1, row=0, sticky=W + N)

        quantity_label = Label(self.frame, text="Qty", bg="white", font=("Helvetica Neue", 15))
        quantity_label.grid(column=2, row=0, sticky=W + N)

        seller_label = Label(self.frame, text="Seller", bg="white", font=("Helvetica Neue", 15))
        seller_label.grid(column=3, row=0, sticky=W + N)

        for item in range(len(self.item_list)):
            self.items_radbtns.append(
                Radiobutton(self.frame, text=self.item_list[item].name, bg="white", value=item,
                            variable=self.item_var))
            self.items_radbtns[item].grid(column=0, row=item + 1, padx=5, sticky=W + N)

            self.price_lbls.append(
                Label(self.frame, text="$" + str(self.item_list[item].price), bg="white", ))
            self.price_lbls[item].grid(column=1, row=item + 1, padx=5, sticky=W + N)

            self.qty_lbls.append(
                Label(self.frame, text=self.item_list[item].qty, bg="white", ))
            self.qty_lbls[item].grid(column=2, row=item + 1, padx=5, sticky=W + N)

            self.seller_lbls.append(
                Label(self.frame, text=self.item_list[item].vendor, bg="white", anchor="w"))
            self.seller_lbls[item].grid(column=3, row=item + 1, padx=5, sticky=W + N)

        # put the frame in the self.canvas
        self.canvas.create_window(0, 0, anchor='nw', window=self.frame)
        # make sure everything is displayed before configuring the scrollregion
        self.canvas.update_idletasks()

        self.canvas.configure(scrollregion=self.canvas.bbox('all'),
                              yscrollcommand=self.scroll_y.set, width=400)

        self.canvas.grid(column=0, row=2, columnspan=4, sticky=E)
        self.scroll_y.grid(column=4, row=2, sticky=N + S)

    def sell_item(self):
        items_sold = simpledialog.askinteger(title="Sell Item Entry", prompt="Enter number of items to be sold")
        current_qty = self.item_list[self.item_var.get()].qty - items_sold
        while self.item_list[self.item_var.get()].qty - items_sold < 0:
            messagebox.showerror("ERROR",
                                 "you have tried to sell more items than in stock please enter a lower integer")
            items_sold = simpledialog.askinteger(title="Sell Item Entry", prompt="Enter number of items to be sold")
            current_qty = 0
        self.item_list[self.item_var.get()].qty = current_qty
        self.qty_lbls[self.item_var.get()].configure(text=current_qty)

    def restock_item(self):
        items_restocked = simpledialog.askinteger(title="Restock Item Entry", prompt="Enter number of items to be "
                                                                                     "Restocked")
        while items_restocked < 0:
            messagebox.showerror("ERROR",
                                 "Input not valid please enter a positive value")
            items_restocked = simpledialog.askinteger(title="Restock Item Entry", prompt="Enter number of items to be "
                                                                                         "Restocked")
        print(self.item_var.get())
        restocked_qty = self.item_list[self.item_var.get()].qty + items_restocked
        self.item_list[self.item_var.get()].qty = restocked_qty
        self.qty_lbls[self.item_var.get()].configure(text=restocked_qty)

    def add_item(self):
        self.splash_screen = Toplevel(root)
        lbl_names = ["Name:", "Price:", "Quantity:", "Vendor:"]
        lbl_list = []

        descrp_lbl = Label(self.splash_screen, text="Please Enter Product Details")
        descrp_lbl.grid(column=0, row=0, columnspan=2, sticky=E + W)

        for name in range(len(lbl_names)):
            lbl_list.append(Label(self.splash_screen, text=lbl_names[name]))
            lbl_list[name].grid(column=0, row=name + 1)

        self.name_var = StringVar()
        self.price_var = StringVar()
        self.qty_var = StringVar()
        self.vendor_var = StringVar()

        name_entry = Entry(self.splash_screen, textvariable=self.name_var)
        name_entry.grid(column=1, row=1)

        price_entry = Entry(self.splash_screen, textvariable=self.price_var)
        price_entry.grid(column=1, row=2)

        qty_entry = Entry(self.splash_screen, textvariable=self.qty_var)
        qty_entry.grid(column=1, row=3)

        vendor_entry = Entry(self.splash_screen, textvariable=self.vendor_var)
        vendor_entry.grid(column=1, row=4)

        submit_btn = Button(self.splash_screen, text="Submit Product", command=self.destroy_splashscreen)
        submit_btn.grid(column=0, row=5, columnspan=2, sticky=E + W, pady=10)

    def destroy_splashscreen(self):
        self.item_list.append(
            Item(self.name_var.get(), int(self.price_var.get()), int(self.qty_var.get()), self.vendor_var.get()))
        self.update_list()
        self.splash_screen.destroy()
        self.splash_screen.update()

    def update_list(self):
        self.items_radbtns.append(
            Radiobutton(self.frame, text=self.item_list[-1].name, bg="white", value=len(self.item_list) - 1,
                        variable=self.item_var))
        self.items_radbtns[-1].grid(column=0, row=len(self.item_list) + 1, padx=5, sticky=W + N)

        self.price_lbls.append(
            Label(self.frame, text="$" + str(self.item_list[-1].price), bg="white", ))
        self.price_lbls[-1].grid(column=1, row=len(self.item_list) + 1, padx=5, sticky=W + N)

        self.qty_lbls.append(
            Label(self.frame, text=self.item_list[-1].qty, bg="white", ))
        self.qty_lbls[-1].grid(column=2, row=len(self.item_list) + 1, padx=5, sticky=W + N)

        self.seller_lbls.append(
            Label(self.frame, text=self.item_list[-1].vendor, bg="white", anchor="w"))
        self.seller_lbls[-1].grid(column=3, row=len(self.item_list) + 1, padx=5, sticky=W + N)

        self.canvas.update_idletasks()

        self.canvas.configure(scrollregion=self.canvas.bbox('all'),
                              yscrollcommand=self.scroll_y.set, width=400)

        print(len(self.item_list))

        # This version displays the correct values and works but breaks when you try and sell a product

    def save_inventory(self):
        pass


if __name__ == '__main__':
    root = Tk()
    main_screen = Inventory_GUI(root)
    root.mainloop()
