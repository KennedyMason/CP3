from abc import ABC, abstractmethod

# main dessert class
class DessertItem(ABC):

    def __init__(self, name,  tax_percent: float = 7.25):
        self.name = name
        self.tax_percent = tax_percent

    def __str__(self):
        return f"The dessert is {self.name}."
    
    def calculate_tax(self, cost):
        return cost * self.tax_percent
    
    @abstractmethod

    def calculate_cost():
        pass


# candy class
class Candy(DessertItem):
    
    def __init__(self, name, candy_weight, price_per_pound):
        super().__init__(name)
        self.candy_weight = candy_weight
        self.price_per_pound = price_per_pound

    def calculate_cost(self):
        return self.candy_weight * self.price_per_pound


# cookie class
class Cookie(DessertItem):
    
    def __init__(self, name, cookie_quantity, price_per_dozen):
        super().__init__(name) 
        self.cookie_quantity = cookie_quantity
        self.price_per_dozen = price_per_dozen

    def calculate_cost(self):
        return self.cookie_quantity * self.price_per_dozen


# ice cream class
class IceCream(DessertItem):

    def __init__(self, name, scoop_count, price_per_scoop):
        super().__init__(name)
        self.scoop_count = scoop_count
        self.price_per_scoop = price_per_scoop

    def calculate_cost(self):
        return self.scoop_count * self.price_per_scoop


# sundae class (ice cream subclass)
class Sundae(IceCream):

    def __init__(self, name, scoop_count, price_per_scoop, topping_name, topping_price):
        super().__init__(name, scoop_count, price_per_scoop)
        self.topping_name = topping_name
        self.topping_price = topping_price


