# ========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def __str__(self):
        return f"This shoe is in {self.country}, code: {self.code}, product: {self.product}, cost: {self.cost}, " \
               f"quantity: {self.quantity}"


# =============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []


# ==========Functions outside the class==============
def read_shoes_data():
    # Function that opens txt file and reads each item to list, classifies each item, creates an object from
    # the variables and appends to the shoe list
    try:
        f = open("inventory.txt", "r", encoding='utf-8')
        for line in f:
            shoe_line = line.split(',')
            country = shoe_line[0]
            code = shoe_line[1]
            product = shoe_line[2]
            cost = shoe_line[3]
            quantity = shoe_line[4]
            shoe_object = Shoe(country, code, product, cost, quantity)
            shoe_list.append(shoe_object)
        f.close()
        # Remove first line from list as it is not a shoe type
        shoe_list.pop(0)
        # Adding new line to last list entry
        shoe_list[-1].quantity += "\n"
        # Removing '\n' from each quantity line for later manipulation
        for shoe in shoe_list:
            shoe.quantity = shoe.quantity[:-1]
    except IndexError:
        print(f"Shoe {line} is missing some data")


def capture_shoes():
    # Function that takes user input for a shoes detail, creates an object and appends to shoe list
    country = input("Please input the country: ")
    code = input("Please input the code: ")
    product = input("Please input the product: ")
    cost = int(input("Please input the cost: "))
    quantity = int(input("Please input the quantity: "))
    shoe_object = Shoe(country, code, product, cost, quantity)
    shoe_list.append(shoe_object)
    #Lastly, the inventory txt file is re-written with new shoe data
    v = open("inventory.txt", "w", encoding='utf-8')
    v.write("Country,Code,Product,Cost,Quantity\n")
    for shoe in shoe_list:
        v.write(f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n")
    v.close()



def view_all():
    # Function that prints the shoe details of each object stored in shoe list
    for shoe in shoe_list:
        print(shoe)


def re_stock():
    # Function that finds the lowest quantity shoe and offers user to restock it
    # If user re-stocks, it updates the shoe list quantity and re-writes to the inventory txt file
    minimum = min(shoe_list, key=lambda shoe: int(shoe.quantity))
    print(f"The lowest quantity shoe is {minimum.product} with {minimum.quantity}")
    restock_check = input("Do you want to restock this shoe? y/n: ")
    while True:
        if restock_check.lower() == 'y':
            restock_order = int(input("Please enter how many pairs to order: "))
            minimum.quantity = restock_order + int(minimum.quantity)

            # Following code rewrites the inventory txt file with the new quantity
            v = open("inventory.txt", "w", encoding='utf-8')
            v.write("Country,Code,Product,Cost,Quantity\n")
            for shoe in shoe_list:
                v.write(f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n")
            v.close()
            break
        elif restock_check.lower() == 'n':
            print("Shoe not restocked")
            break
        else:
            restock_check = (input("Incorrect response. Do you want to restock this shoe? y/n "))


def search_shoe():
    # Function that takes in shoe code and finds and prints shoe that matches code from shoe_list
    shoe_code = input("Please enter shoe code: ")
    found_code = 0
    for shoe in shoe_list:
        if shoe.code == shoe_code:
            print(shoe)
            found_code = 1
        else: found_code = 0
    if found_shoe == 0:
        print("Shoe code entered not found.")

def search_shoe_product():
    # Function that takes in shoe code and finds and prints shoe that matches code from shoe_list
    shoe_product = input("Please enter shoe product name: ")
    found_shoe = 0
    # Loop through list and print shoe product if found
    for shoe in shoe_list:
        if shoe.product == shoe_product:
            print(shoe)
            found_shoe = 1
        else: found_shoe = 0
    if found_shoe == 0:
        print("Shoe product entered not found.")


def value_per_item():
    # Calculates and prints the value (cost * quantity) for each shoe
    for shoe in shoe_list:
        value = int(shoe.quantity) * int(shoe.cost)
        print(f"Shoe: {shoe.product}, Value: {value}")


def highest_qty():
    # Function finds the shoe in shoe list with highest quantity
    maximum = max(shoe_list, key=lambda shoe: int(shoe.quantity))
    print(f"{maximum.product} is on sale!")



#==========Main Menu=============

read_shoes_data()

while True:
    menu_select = input("""
    Select option from the menu:
    a - Update shoe list from inventory
    b - Enter shoe into inventory
    c - Display inventory list
    d - Find lowest quantity product to re-stock
    e - Find shoe details by code
    f - Find shoe details by product name
    g - Display shoe list stock values
    h - Find highest quantity product to put on sale
    i - Quit
    """)

    if menu_select.lower() == 'a':
        read_shoes_data()

    elif menu_select.lower() == 'b':
        capture_shoes()

    elif menu_select.lower() == 'c':
        view_all()

    elif menu_select.lower() == 'd':
        re_stock()

    elif menu_select.lower() == 'e':
        search_shoe()

    elif menu_select.lower() == 'f':
        search_shoe_product()

    elif menu_select.lower() == 'g':
        value_per_item()

    elif menu_select.lower() == 'h':
        highest_qty()

    elif menu_select.lower() == 'i':
        break

    else:
        print("Invalid selection. Try again: ")


