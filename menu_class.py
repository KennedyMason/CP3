import os

def clear():   
    os.system('cls' if os.name == 'nt' else 'clear')
    
class Order:

    drink_menu = {"Water" : 0.50,
                  "Dr Pepper" : 1.20,
                  "Coca Cola" : 1.20,
                  "Sprite" : 1.00,
                  "Apple Juice" : 0.75}
    
    app_menu = {"Fries" : 2.50,
                "Tater Tots" : 3.25,
                "Breadsticks" : 3.50,
                "Chips" : 2.00}
    
    main_menu = {"Pizza" : 8.00,
                 "Burger" : 6.00,
                 "Steak" : 10.00,
                 "Sandwich" : 5.00}
    
    side_menu = {"Salad" : 4.00,
                 "Soup" : 4.50,
                 "Baked Potato" : 4.25}
    
    dessert_menu = {"Cake Slice" : 4.00,
                    "Ice Cream" : 3.50,
                    "Brownie": 2.50,
                    "Cookie" : 2.00}

    def __init__(self, drink, app, main, side1, side2, dessert):
        self.drink = drink
        self.app = app
        self.main = main
        self.side1 = side1
        self.side2 = side2
        self.dessert = dessert

    def __str__(self):
        return f"\nYour order is:\n Drink: {self.drink}\n Appetizer: {self.app}\n Main Course: {self.main}\n Side 1: {self.side1}\n Side 2: {self.side2}\n Dessert: {self.dessert}"
    
    
    def order_total(self):

        if self.drink == "None":
            drink = 0
        else:
            drink = Order.drink_menu[self.drink.title()]
        
        if self.app == "None":
            app = 0
        else:
            app = Order.app_menu[self.app.title()]

        if self.main == "None":
            main = 0
        else:
            main = Order.main_menu[self.main.title()]

        if self.side1 == "None":
            side1 = 0
        else:
            side1 = Order.side_menu[self.side1.title()]

        if self.side2 == "None":
            side2 = 0
        else:
            side2 = Order.side_menu[self.side2.title()]

        if self.dessert == "None":
            dessert = 0
        else:
            dessert = Order.dessert_menu[self.dessert.title()]

        total = drink + app + main + side1 + side2 + dessert

        return f"Your total is ${total}."


drink_choice = ""
app_choice = ""
main_choice = ""
side1_choice = ""
side2_choice = ""
dessert_choice = ""

def view_menu():

    looking = True
    
    print("\nThere are five menus:\n\
a. Drinks\n\
b. Appetizers\n\
c. Main Courses\n\
d. Sides\n\
e. Desserts")

    while looking == True:
    
        menu_type = input("\nWhich menu would you like to view? (letter): ")
        
        if menu_type.lower(). == "a":
            
            print("\nDrink menu:")
            print("\n".join("{}\t{}".format(k, v) for k, v in Order.drink_menu.items()))
            
        elif menu_type.lower(). == "b":
            
            print("\nAppetizer menu: ")
            print("\n".join("{}\t{}".format(k, v) for k, v in Order.app_menu.items()))
            
        elif menu_type.lower(). == "c":
            
            print("\nMain course menu: ")
            print("\n".join("{}\t{}".format(k, v) for k, v in Order.main_menu.items()))
            
        elif menu_type.lower(). == "d":
            
            print("\nSide menu: ")
            print("\n".join("{}\t{}".format(k, v) for k, v in Order.side_menu.items()))
            
        elif menu_type.lower(). == "e":
            
            print("\nDessert menu: ")
            print("\n".join("{}\t{}".format(k, v) for k, v in Order.dessert_menu.items()))
            
        contin = input("\nWould you like to keep looking? (y/n): ")
        
        if contin == "n":
            looking = False


def take_order():
    
    global drink_choice
    global app_choice
    global main_choice
    global side1_choice
    global side2_choice
    global dessert_choice
    
    ordered = False
    
    print("\nIf you do not wish to order an item, please enter 'None'.\n")
    
    while ordered == False:
    
        #choose drink
        drink_choice = input("Enter drink choice: ")
        
        while drink_choice.title() not in Order.drink_menu or drink_choice.title() != "None":
            
            print("\nPlease enter and item from the drink menu.")
            drink_choice = input("\nEnter drink choice: ")
            
            
        #choose appetizer
        app_choice = input("Enter appetizer choice: ")
        
        while app_choice.title() not in Order.app_menu or app_choice.title() != "None":
            
            print("\nPlease enter and item from the appetizer menu.")
            app_choice = input("\nEnter appetizer choice: ")
            
        
        #choose main course
        main_choice = input("Enter main course choice: ")
        
        while main_choice.title() not in Order.main_menu or main_choice.title() != "None":
            
            print("\nPlease enter and item from the main course menu.")
            main_choice = input("\nEnter main course choice: ")
            
        
        #choose first side 
        side1_choice = input("Enter first side choice: ")
        
        while side1_choice.title() not in Order.side_menu or _choice.title() != "None":
            
            print("\nPlease enter and item from the side menu.")
            side1_choice = input("\nEnter first side choice: ")
        
    
        #choose second side
        side2_choice = input("Enter second side choice: ")
    
        while side2_choice.title() not in Order.side_menu:
        
            print("\nPlease enter and item from the side menu.")
            side2_choice = input("\nEnter second side choice: ")
        
        #choose dessert
        dessert_choice = input("Enter dessert choice: ")
    
        while dessert_choice.title() not in Order.dessert_menu:
        
            print("\nPlease enter and item from the dessert menu.")
            dessert_choice = input("\nEnter dessert choice: ")
            
        complete = input("Complete your order? (y/n): ")
        
        if complete == "y":
            ordered = True

see_menu = input("Welcome to Kennedy's Restaurant! Would you like to see a menu? (y/n): ")
if see_menu == "y":
    view_menu()

take_order()

order = Order(drink_choice, app_choice, main_choice, side1_choice, side2_choice, dessert_choice)

print(order.__str__())
print(order.order_total())