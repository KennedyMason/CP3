



class Order:

    order

    def __init__(self, drink, app, main, side1, side2, dessert):
        self.drink = drink
        self.app = app
        self.main = main
        self.side1 = side1
        self.side2 = side2
        self.dessert = dessert

    def __str__(self):
        return f"Your order is:\n Drink: {self.drink}\n Appetizer: {self.app}\n Main Course: {self.main}\n Side 1: {self.side1}\n Side 2: {self.side2}\n Dessert: {self.dessert}"
    
    def check_contents(self):
        if self.
    


def take_order:

    print("Welcome to Kennedy's Restauarnt!")

    want_drink = input("Would you like a drink? (y/n)")

        if want_drink == "y":
            drink = input("Which drink?: ")

        elif want_drink == "n":
            drink = "None"