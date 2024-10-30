
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
            print(f"{item}")
        
    def add(self, item):
        self.order.append(item.name)
      
    def total_items(self):
        total = len(self.order)
        return total


def main():

    order = Order([])
    
    order.add(Candy("Candy Corn", 1.5, .25))
    order.add(Candy("Gummy Bears", .25, .35))
    order.add(Cookie("Chocolate Chip", 6, 3.99))
    order.add(IceCream("Pistachio", 2, .79))
    order.add(Sundae("Vanilla", 3, .69, "Hot Fudge", 1.29))
    order.add(Cookie("Oatmeal Raisin", 2, 3.45))

    print(order.__str__())
    print(f'Total number of items in order: {order.total_items()}')
 
main()