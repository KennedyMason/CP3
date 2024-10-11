

class Order:

    drink_menu = {"Water" : 0.50,
                  "Dr. Pepper" : 1.20,
                  "Coca-Cola" : 1.20,
                  "Sprite" : 1.00,
                  "Apple Juice" : 0.75}
    
    app_menu = {"Fries" : 2.50,
                "Tater-Tots" : 3.25,
                "Breadsticks" : 3.50,
                "Chips and Salsa" : 2.00}
    
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
        return f"Your order is:\n Drink: {self.drink}\n Appetizer: {self.app}\n Main Course: {self.main}\n Side 1: {self.side1}\n Side 2: {self.side2}\n Dessert: {self.dessert}"
    
    
    def order_total(self):
        drink = Order.drink_menu[self.drink.title()]
        app = Order.app_menu[self.app.title()]
        main = Order.main_menu[self.main.title()]
        side1 = Order.side_menu[self.side1.title()]
        side2 = Order.side_menu[self.side2.title()]
        dessert = Order.dessert_menu[self.dessert.title()]

        total = drink + app + main + side1 + side2 + dessert

        return f"Your total is ${total}."


def take_order():

    print("Hello! Welcome to Kennedy's Restaurant\n")

    need_menu = ("Would you like to see the menu? (y/n): ")

    if need_menu.lower() == "y":

        print("There are five menus:\n\
a. Drinks\n\
b. ")

order = Order("Water", "Fries", "Pizza", "Salad", "Baked Potato", "Ice Cream")

print(order.order_total())






