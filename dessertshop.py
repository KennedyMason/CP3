
# main dessert class
class DessertItem:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"The dessert is {self.name}."
    


# candy class
class Candy(DessertItem):
    
    def __init__(self, name, candy_weight, price_per_pound):
        super().__init__(name)
        self.candy_weight = candy_weight
        self.price_per_pound = price_per_pound



# cookie class
class Cookie(DessertItem):
    
    cookie_menu = {"Chocalate Chip" : 18.00,
                   "Snickerdoodle" : 24.00,
                    "Oatmeal" : 12.00}
    
    def __init__(self, name, cookie_quantity, price_per_dozen):
        super().__init__(name) 
        self.cookie_quantity = cookie_quantity
        self.price_per_dozen = price_per_dozen



# ice cream class
class IceCream(DessertItem):

    def __init__(self, name, scoop_count, price_per_scoop):
        super().__init__(name)
        self.scoop_count = scoop_count
        self.price_per_scoop = price_per_scoop



# sundae class (ice cream subclass)
class Sundae(IceCream):

    def __init__(self, name, scoop_count, price_per_scoop, topping_name, topping_price):
        super().__init__(name, scoop_count, price_per_scoop)
        self.topping_name = topping_name
        self.topping_price = topping_price




# class that makes order
class Order:

    def __init__(self, order = []):
        self.order = order

    def __str__(self):
        for item in self.order:
            return f"{item}"
        
    def add(self, item):
        self.order.append(item)
    
    def total_items(self):
        total = len(self.order)
        return f"{total}"



def main():

    order = Order([])

    order.add(Candy("Gummy Bears", 5, 2.00))
    order.add(Cookie("Chocolate Chip", 12, 18.00))
    order.add(IceCream("Vanilla", 2, 0.50))
    order.add(Sundae("Chocolate", 3, 1.00, "Syrup", 1.00))

    item_amount = order.total_items

    print(order)
    print(f"Total number of items: {item_amount}")


main()