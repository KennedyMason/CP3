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

        if self.drink.title() == "None":
            drink = 0
        else:
            drink = Order.drink_menu[self.drink.title()]
        
        if self.app.title() == "None":
            app = 0
        else:
            app = Order.app_menu[self.app.title()]

        if self.main.title() == "None":
            main = 0
        else:
            main = Order.main_menu[self.main.title()]

        if self.side1.title() == "None":
            side1 = 0
        else:
            side1 = Order.side_menu[self.side1.title()]

        if self.side2.title() == "None":
            side2 = 0
        else:
            side2 = Order.side_menu[self.side2.title()]

        if self.dessert.title() == "None":
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
        
        if menu_type.lower().strip() == "a":
            
            print("\nDrink menu:")
            print("\n".join("{}\t{}".format(k, v) for k, v in Order.drink_menu.items()))
            
        elif menu_type.lower().strip() == "b":
            
            print("\nAppetizer menu: ")
            print("\n".join("{}\t{}".format(k, v) for k, v in Order.app_menu.items()))
            
        elif menu_type.lower().strip() == "c":
            
            print("\nMain course menu: ")
            print("\n".join("{}\t{}".format(k, v) for k, v in Order.main_menu.items()))
            
        elif menu_type.lower().strip() == "d":
            
            print("\nSide menu: ")
            print("\n".join("{}\t{}".format(k, v) for k, v in Order.side_menu.items()))
            
        elif menu_type.lower().strip() == "e":
            
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
    items = 0
    
    print("\nIf you do not wish to order an item, please enter 'None'.\n")
    
    while ordered == False:
    
        #choose drink
        drink_choice = input("Enter drink choice: ")
        
        while drink_choice.strip().title() not in Order.drink_menu and drink_choice.strip().title() != "None":
            
            print("\nPlease enter an item from the drink menu.")
            drink_choice = input("\nEnter drink choice: ")
            
        if drink_choice.title() != "None":
            items += 1
            
            
        #choose appetizer
        app_choice = input("Enter appetizer choice: ")
        
        while app_choice.strip().title() not in Order.app_menu and app_choice.strip().title() != "None":
            
            print("\nPlease enter an item from the appetizer menu.")
            app_choice = input("\nEnter appetizer choice: ")
            
        if app_choice.title() != "None":
            items += 1
        
        #choose main course
        main_choice = input("Enter main course choice: ")
        
        while main_choice.strip().title() not in Order.main_menu and main_choice.strip().title() != "None":
            
            print("\nPlease enter an item from the main course menu.")
            main_choice = input("\nEnter main course choice: ")
            
        if main_choice.title() != "None":
            items += 1
            
        #choose first side 
        side1_choice = input("Enter first side choice: ")
        
        while side1_choice.strip().title() not in Order.side_menu and side1_choice.strip().title() != "None":
            
            print("\nPlease enter an item from the side menu.")
            side1_choice = input("\nEnter first side choice: ")
        
        if side1_choice.title() != "None":
            items += 1
            
        #choose second side
        side2_choice = input("Enter second side choice: ")
    
        while side2_choice.strip().title() not in Order.side_menu and side2_choice.strip().title() != "None":
        
            print("\nPlease enter an item from the side menu.")
            side2_choice = input("\nEnter second side choice: ")
    
        if side2_choice.title() != "None":
            items += 1
        
        #choose dessert
        dessert_choice = input("Enter dessert choice: ")
    
        while dessert_choice.strip().title() not in Order.dessert_menu and dessert_choice.strip().title() != "None":
        
            print("\nPlease enter an item from the dessert menu.")
            dessert_choice = input("\nEnter dessert choice: ")
            
        if dessert_choice.title() != "None":
            items += 1
            
        complete = input("\nComplete your order? (y/n): ")
        
        while complete.lower() != "y" and complete.lower() != "n": 
            print("\nInvalid response.")
            complete = input("\nComplete your order? (y/n): ")

        if complete == "y":
            
            if items == 0:
                print("\nYou haven't ordered anything! Order at least one item to continue.\n")
                
            else:
                ordered = True

        #change item in order
        elif complete =="n":
            change = input("Which category would you like to change?: ")

            #change drink
            if change.lower() == "drink":

                items -=1
                drink_choice = input("Enter drink choice: ")
        
                while drink_choice.strip().title() not in Order.drink_menu and drink_choice.strip().title() != "None":
            
                    print("\nPlease enter an item from the drink menu.")
                    drink_choice = input("\nEnter drink choice: ")
            
                if drink_choice.title() != "None":
                    items += 1

            
            #change appetizer
            elif change.lower() == "appetizer":

                items -= 1
                app_choice = input("Enter appetizer choice: ")
        
                while app_choice.strip().title() not in Order.app_menu and app_choice.strip().title() != "None":
                    
                    print("\nPlease enter an item from the appetizer menu.")
                    app_choice = input("\nEnter appetizer choice: ")
                    
                if app_choice.title() != "None":
                    items += 1


            #change main course
            elif change.lower().strip() == "maincourse":

                items -= 1
                main_choice = input("Enter main course choice: ")
                            
                while main_choice.strip().title() not in Order.main_menu and main_choice.strip().title() != "None":
                                
                    print("\nPlease enter an item from the main course menu.")
                    main_choice = input("\nEnter main course choice: ")
                                
                if main_choice.title() != "None":
                    items += 1


        
            #change side
            elif change.lower() == "side" or change.lower().strip() == "side1" or change.lower().strip() == "side2":

                if change.lower() == "side":
                    which_side = input("Which side? (1 or 2): ")

                    while which_side != "1" or which_side != "2":
                        print("Invalid response. Try again.")
                        which_side = input("Which side? (1 or 2): ")

                #side 1
                if change.lower().strip() == "side1" or which_side == "1":

                    items -= 1
                    side1_choice = input("Enter first side choice: ")
                    
                    while side1_choice.strip().title() not in Order.side_menu and side1_choice.strip().title() != "None":
                        
                        print("\nPlease enter an item from the side menu.")
                        side1_choice = input("\nEnter first side choice: ")
                    
                    if side1_choice.title() != "None":
                        items += 1


                #side 2
                if change.lower().strip() == "side2" or which_side == "2":

                    items -= 1
                    side2_choice = input("Enter second side choice: ")
                
                    while side2_choice.strip().title() not in Order.side_menu and side2_choice.strip().title() != "None":
                    
                        print("\nPlease enter an item from the side menu.")
                        side2_choice = input("\nEnter second side choice: ")
                
                    if side2_choice.title() != "None":
                        items += 1
                
            
            #change dessert
            elif change.lower() == "dessert":

                items -= 1
                dessert_choice = input("Enter dessert choice: ")
            
                while dessert_choice.strip().title() not in Order.dessert_menu and dessert_choice.strip().title() != "None":
                
                    print("\nPlease enter an item from the dessert menu.")
                    dessert_choice = input("\nEnter dessert choice: ")
                    
                if dessert_choice.title() != "None":
                    items += 1

            
            #don't change
            elif change.lower() == "none":
                ordered = True

    






            

see_menu = input("Welcome to Kennedy's Restaurant! Would you like to see a menu? (y/n): ")
if see_menu == "y":
    view_menu()

take_order()

order = Order(drink_choice, app_choice, main_choice, side1_choice, side2_choice, dessert_choice)

print(order.__str__())
print()
print(order.order_total())