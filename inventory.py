# L1T30 - Capstone IV.


#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = int(cost)
        self.quantity = int(quantity)


    def get_cost(self):
        return self.cost
     

    def get_quantity(self):
        return self.quantity
    

    def __str__(self):
        return (f"The {self.product} shoe from {self.country} and {self.code} code "
        f"is priced at R {self.cost} and has {self.quantity} in stock.")
      


#=============Shoe list===========


#The list will be used to store a list of objects of the 'Shoe' Class readed 
# from the 'inventory.txt' file.
shoe_list = []

#==========Functions outside the class==============

# Each line of the 'inventory.txt' file will be saved as a Shoe class object.
def read_shoes_data():
    
    try:
        with open("inventory-info.txt", "r", encoding='utf-8-sig') as file_data:
            lines = file_data.readlines()
            del lines[0]
        
        for shoe in lines:
            shoe = shoe.strip("\n")
            shoe = shoe.split(",")
            shoe = Shoe(shoe[0], shoe[1], shoe[2], shoe[3], shoe[4])
            shoe_list.append(shoe)
          
    # If the inventory.txt file does not exist for reading, the Exception will run.
    except Exception:
        print("There was an error opening the text file, please try again")

# a New Class Shoe object is created and appended to the 'shoe_list', aswell as
# printed on a new line in the 'inventory.txt' file.
def capture_shoes():
    country = (input(f"Please enter country name: "))
    code = (input(f"Please enter shoe code eg.SKU20394: "))
    product = (input(f"Please enter shoe product name: "))

    while True:
        try:
            cost = int(input(f"Please enter shoe cost: "))
            break
     
        except Exception:
            print("Please enter a integer value")

    while True:
        try:
            quantity = int(input(f"Please enter shoe quantity: "))
            break
       
        except Exception:
            print("Please enter a integer value")

    new_shoe_object = Shoe(country, code, product, cost, quantity)
    shoe_list.append(new_shoe_object)

    with open("inventory-info.txt", "a", encoding='utf-8-sig') as txt_file:
        txt_file.write(f"\n{new_shoe_object.country},{new_shoe_object.code},"
        f"{new_shoe_object.product},{new_shoe_object.cost},{new_shoe_object.quantity}")
     

# Each Shoe object is printed as per the '__str__' Shoe method.
def view_all():
    for i in range(len(shoe_list)):
        print(shoe_list[i].__str__())



def re_stock():
    small = shoe_list[0].quantity
    product_code = shoe_list[0].code

    for i in range(len(shoe_list)):
    
        if shoe_list[i].quantity < small:
            small = shoe_list[i].quantity
            product_code = shoe_list[i].code

    while True:
        try:        
            add_val = int(input(
                f"How many do you want to add to the product {product_code} with the lowest quantity of {small}? "))
            break

        except Exception:
            print("Please enter a integer eg. 16")

    new_qty = (add_val + small)

    for shoe in shoe_list:
        if shoe.code == product_code:
            shoe.quantity = new_qty
    # Please note, the new quantity list is printed to a new txt file not to 
    # disrupt the original txt file. 
    with open("inventory-info.txt", "w") as txt_file:
        txt_file.write("Country,Code,Product,Cost,Quantity")
        txt_file.write("\n")
        for shoe in shoe_list:
            shoe_string = f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}"
            txt_file.write(shoe_string)
            txt_file.write("\n")



def seach_shoe():

    while True:
        try:

            shoe_name = input("Please enter shoe code: ")
            for shoe in shoe_list:
                if shoe_name == shoe.code:
                    print(f"\n{shoe.__str__()}")
                    return
            
            print("Invalid code, try again")
                
        except Exception:
            print("You have entered an invalid shoe code, try again...")

    

def value_per_item():
    for shoe in shoe_list:
        value = (shoe.cost * shoe.quantity)
        print(f"{shoe.product}'s value = R {value}")



def highest_qty():

    large = shoe_list[0].quantity
    product_code = shoe_list[0].code

    for i in range(len(shoe_list)):
    
        if shoe_list[i].quantity > large:
            large = shoe_list[i].quantity
            product_code = shoe_list[i].product

    print(f"The {product_code}'s are on SALE!!")

   

#==========Main Menu=============



user_message = '''
Welcome to the shoe inventory system! What would you like to do?

r - read_shoes_data.
c - capture_shoes.
va - view_all.
re - re_stock.
ss - seach_shoe.
v - value_per_item.
hi - highest_qty.
e - exit this program.
'''

while True:
    user_choice = input(user_message).strip().lower()

    if user_choice == "r":
        read_shoes_data()

    elif user_choice == "c":
        capture_shoes()

    elif user_choice == "va":
        view_all()

    elif user_choice == "re":
        re_stock()

    elif user_choice == "ss":
        seach_shoe()

    elif user_choice == "v":
        value_per_item()

    elif user_choice == "hi":
        highest_qty()

    elif user_choice == "e":
        print("Exiting, Bye for now...")
        break

    else:
        print("Oops - incorrect input, try again...")



# End of program. 