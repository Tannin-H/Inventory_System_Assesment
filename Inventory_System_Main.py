from tkinter import *
import pickle
from tkinter import messagebox
from tkinter import simpledialog

# creating a support class that is used to fill in the relevant fields for each item
class Item:
    def __init__(self, name, price, qty, vendor):
        self.name = name
        self.price = price
        self.qty = qty
        self.vendor = vendor


# main class handling GUI operations
class Inventory_GUI:
    def __init__(self, parent):
        # importing the items from the data base as self.item_list
        pickle_in = open("inventory_database", "rb")
        self.item_list = pickle.load(pickle_in)
        pickle_in.close()
        # initialising item var and lists for labels
        self.item_var = IntVar()
        self.items_radbtns = []
        self.price_lbls = []
        self.qty_lbls = []
        self.seller_lbls = []

        # creates the sell, restock, add item and save inventory buttons and placing them along the top bar
        sell_btn = Button(parent, text="Sell", command=self.sell_item)
        sell_btn.grid(column=0, row=0, sticky=E + W + N)

        restock_btn = Button(parent, text="Restock", command=self.restock_item)
        restock_btn.grid(column=1, row=0, sticky=E + W + N)

        add_btn = Button(parent, text="Add New Item", command=self.add_item)
        add_btn.grid(column=2, row=0, sticky=E + W + N)

        save_btn = Button(parent, text="Save Inventory", command=self.save_inventory)
        save_btn.grid(column=3, row=0, sticky=E + W + N)

        # creates the canvas containing a frame where the products are going to be shown allowing you to scroll
        # through the items
        self.canvas = Canvas(parent)
        self.scroll_y = Scrollbar(parent, orient="vertical", command=self.canvas.yview)

        self.frame = Frame(self.canvas, bg="white")

        # creating the inventory items fields and packing them into the frame
        product_label = Label(self.frame, text="Product", bg="white", font=("Helvetica Neue", 15))
        product_label.grid(column=0, row=0, sticky=W + N)

        price_label = Label(self.frame, text="Price", bg="white", font=("Helvetica Neue", 15))
        price_label.grid(column=1, row=0, sticky=W + N)

        quantity_label = Label(self.frame, text="Qty", bg="white", font=("Helvetica Neue", 15))
        quantity_label.grid(column=2, row=0, sticky=W + N)

        seller_label = Label(self.frame, text="Seller", bg="white", font=("Helvetica Neue", 15))
        seller_label.grid(column=3, row=0, sticky=W + N)
        # looping through and creating all the clickable radio buttons
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

    # handles all the logic when the sell item button is clicked
    def sell_item(self):
        try:
            # ask the user to enter number of items to be sold only accepting ints
            items_sold = simpledialog.askinteger(title="Sell Item Entry", prompt="Enter number of items to be sold")
            # input validation so that - values and 0 are not accepted and displays a message box
            while items_sold <= 0:
                messagebox.showerror("ERROR",
                                     "Input not valid please enter a positive value excluding 0")
                items_sold = simpledialog.askinteger(title="Sell Item Entry", prompt="Enter number of items to be sold")
            # updates the current qty based on the number of items entered to be sold
            current_qty = self.item_list[self.item_var.get()].qty - items_sold
            # validation to prevent user from selling more items than in stock and prompts them to enter the another
            # value
            while self.item_list[self.item_var.get()].qty - items_sold < 0:
                messagebox.showerror("ERROR",
                                     "you have tried to sell more items than in stock please enter a lower integer")
                items_sold = simpledialog.askinteger(title="Sell Item Entry", prompt="Enter number of items to be sold")
                current_qty = 0
            # updates the current qty value to the self.items list and displays that on the label in the frame
            self.item_list[self.item_var.get()].qty = current_qty
            self.qty_lbls[self.item_var.get()].configure(text=current_qty)
        # try except to prevent error when red x or cancel button is pressed
        except TypeError:
            pass

    def restock_item(self):
        try:
            # asks the user to enter number of items t be restocked
            items_restocked = simpledialog.askinteger(title="Restock Item Entry", prompt="Enter number of items to be "
                                                                                         "Restocked")
            # checks if the values entered is = or < 0and if it is asks them to re enter a value
            while items_restocked <= 0:
                messagebox.showerror("ERROR",
                                     "Input not valid please enter a positive value excluding 0")
                items_restocked = simpledialog.askinteger(title="Restock Item Entry",
                                                          prompt="Enter number of items to be "
                                                                 "Restocked")
            # updates the restocked qty and then applies that to the items list which is then displayed
            restocked_qty = self.item_list[self.item_var.get()].qty + items_restocked
            self.item_list[self.item_var.get()].qty = restocked_qty
            self.qty_lbls[self.item_var.get()].configure(text=restocked_qty)
        # try except to prevent error when red x or cancel button is pressed
        except TypeError:
            pass

    def add_item(self):
        # creates a top level screen(new window)
        self.splash_screen = Toplevel(root)
        # sets up lists for for loop label generation
        lbl_names = ["Name:", "Price:", "Quantity:", "Vendor:"]
        lbl_list = []
        # creates heading label and grids it
        descrp_lbl = Label(self.splash_screen, text="Please Enter Product Details")
        descrp_lbl.grid(column=0, row=0, columnspan=2, sticky=E + W)
        # creates the entry field labels
        for name in range(len(lbl_names)):
            lbl_list.append(Label(self.splash_screen, text=lbl_names[name]))
            lbl_list[name].grid(column=0, row=name + 1)
        # initiates entry field variables creates entry fields and grids them
        self.name_var = StringVar()
        self.price_var = StringVar()
        self.qty_var = StringVar()
        self.vendor_var = StringVar()

        name_entry = Entry(self.splash_screen, textvariable=self.name_var)
        name_entry.grid(column=1, row=1)

        price_entry = Entry(self.splash_screen, textvariable=self.price_var)
        price_entry.grid(column=1, row=2)

        # connects float validation to price entry widget and validates with every key stroke by preventing the key
        # from being entered if the returned value is false
        float_val = root.register(check_float)
        price_entry.config(validate="key", validatecommand=(float_val, '%P'))

        qty_entry = Entry(self.splash_screen, textvariable=self.qty_var)
        qty_entry.grid(column=1, row=3)

        # connects int validation to quantity entry widget and validates with every key stroke by preventing the key
        # from being entered if the returned value is false
        int_val = root.register(check_int)
        qty_entry.config(validate="key", validatecommand=(int_val, '%P'))

        vendor_entry = Entry(self.splash_screen, textvariable=self.vendor_var)
        vendor_entry.grid(column=1, row=4)

        # creates the cancel and submit butoons sets the commands and grids them
        cancel_btn = Button(self.splash_screen, text="Cancel", command=self.close_splashscreen)
        cancel_btn.grid(column=0, row=5, sticky=E + W, pady=10)

        submit_btn = Button(self.splash_screen, text="Submit Product", command=self.destroy_splashscreen_save)
        submit_btn.grid(column=1, row=5, sticky=E + W, pady=10)

    # function applied when cancel button is clicked and closes the window without saving the data
    def close_splashscreen(self):
        self.splash_screen.destroy()
        self.splash_screen.update()

    # function called when the submit button is clicked
    def destroy_splashscreen_save(self):
        # checks if any of the fields are empty creates message box if any are
        if self.name_var.get() == "" or self.price_var.get() == "" or self.qty_var.get() == "" or self.vendor_var.get() == "":
            messagebox.showerror("ERROR", "You have left one or more of the required fields blank")
        else:
            # if no fields are empt it appends a new instance of the item class to the item list populated with data
            # from the entry fields
            self.item_list.append(
                Item(self.name_var.get(), float(self.price_var.get()), int(self.qty_var.get()), self.vendor_var.get()))
            # calls update list function
            self.update_list()
            # closes the top level window
            self.splash_screen.destroy()
            self.splash_screen.update()

    def update_list(self):
        # appends a new radio button to the item_radbtns list and grids the new button using the last item in
        # item_list to populate text and value fields
        self.items_radbtns.append(
            Radiobutton(self.frame, text=self.item_list[-1].name, bg="white", value=len(self.item_list) - 1,
                        variable=self.item_var))
        self.items_radbtns[-1].grid(column=0, row=len(self.item_list) + 1, padx=5, sticky=W + N)

        # appends a new price label to the price_lbls list and grids the new label using the last item in
        # item_list to populate text
        self.price_lbls.append(
            Label(self.frame, text="$" + str(self.item_list[-1].price), bg="white", ))
        self.price_lbls[-1].grid(column=1, row=len(self.item_list) + 1, padx=5, sticky=W + N)

        # appends a new qty label to the qty_lbls list and grids the new label using the last item in
        # item_list to populate text
        self.qty_lbls.append(
            Label(self.frame, text=self.item_list[-1].qty, bg="white", ))
        self.qty_lbls[-1].grid(column=2, row=len(self.item_list) + 1, padx=5, sticky=W + N)

        # appends a new seller label to the seller_lbls list and grids the new label using the last item in
        # item_list to populate text
        self.seller_lbls.append(
            Label(self.frame, text=self.item_list[-1].vendor, bg="white", anchor="w"))
        self.seller_lbls[-1].grid(column=3, row=len(self.item_list) + 1, padx=5, sticky=W + N)

        # updates the scroll region
        self.canvas.update_idletasks()

        self.canvas.configure(scrollregion=self.canvas.bbox('all'),
                              yscrollcommand=self.scroll_y.set, width=400)

    # activated when save inventory button is clicked open inventory database file writes the item_list list to the
    # file then closes file and displays pop up confirming save
    def save_inventory(self):
        pickle_out = open("inventory_database", "wb")
        pickle.dump(self.item_list, pickle_out)
        pickle_out.close()
        messagebox.showinfo("Inventory", "Inventory has been saved to file")


# called when running the add new item window to the price field and trys' to convert the character to a float and
# returns true if it is possible and false if its impossible
def check_float(float_input_entry):
    try:
        float(float_input_entry)
        return True
    except ValueError:
        return False


# called when running the add new item window to the quantity field and try's to convert the character to a int and
# returns true if it is possible and false if its impossible
def check_int(int_input_entry):
    try:
        int(int_input_entry)
        return True
    except ValueError:
        return False


# designates where the code runs and initiates the GUI window
if __name__ == '__main__':
    root = Tk()
    main_screen = Inventory_GUI(root)
    root.mainloop()
