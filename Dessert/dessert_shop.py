from abc import ABC, abstractmethod
from receipt import *


# main dessert class
class DessertItem(ABC):

    def __init__(self, name,  tax_percent: float = 7.25):
        self.name = name
        self.tax_percent = tax_percent

    def __str__(self):
        return f"{self.name}"
    
    def calculate_tax(self, cost):
        tax = cost * self.tax_percent
        return round(tax, 2)
    
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
        cost =self.candy_weight * self.price_per_pound
        return round(cost, 2)

# cookie class
class Cookie(DessertItem):
    
    def __init__(self, name, cookie_quantity, price_per_dozen):
        super().__init__(name) 
        self.cookie_quantity = cookie_quantity
        self.price_per_dozen = price_per_dozen

    def calculate_cost(self):
        cost = self.cookie_quantity * self.price_per_dozen
        return round(cost, 2)

# ice cream class
class IceCream(DessertItem):

    def __init__(self, name, scoop_count, price_per_scoop):
        super().__init__(name)
        self.scoop_count = scoop_count
        self.price_per_scoop = price_per_scoop

    def calculate_cost(self):
        cost = self.scoop_count * self.price_per_scoop
        return round(cost, 2)

# sundae class (ice cream subclass)
class Sundae(IceCream):

    def __init__(self, name, scoop_count, price_per_scoop, topping_name, topping_price):
        super().__init__(name, scoop_count, price_per_scoop)
        self.topping_name = topping_name
        self.topping_price = topping_price

    def calculate_cost(self):
        cost = (self.scoop_count * self.price_per_scoop) + self.topping_price
        return round(cost, 2)
    
