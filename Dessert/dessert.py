from abc import ABC, abstractmethod

class DessertItem(ABC):
    def __init__(self,name):
        self.name = name
        self.tax_percent = .0725

    @abstractmethod

    def calculate_cost(self):
        pass
    
    def calculate_tax(self):
        tax = self.calculate_cost() * (self.tax_percent)
        return tax

class Candy(DessertItem):
    def __init__(self,name,candy_weight,price_per_pound):
        super().__init__(name)
        self.candy_weight = candy_weight
        self.price_per_pound = price_per_pound

    def __str__(self):
        return f'{self.name}, {self.candy_weight}lbs, ${self.price_per_pound}/lb, ${self.calculate_cost}, {self.calculate_tax}'

    def calculate_cost(self):
        cost = self.candy_weight * self.price_per_pound
        return cost

class Cookie(DessertItem):
    def __init__(self,name,cookie_quantity,price_per_dozen):
        super().__init__(name)
        self.cookie_quantity = cookie_quantity
        self.price_per_dozen = price_per_dozen

    def __str__(self):
        return f'{self.name}, {self.cookie_quantity} cookies, ${self.price_per_dozen}/dozen, ${self.calculate_cost}, {self.calculate_tax}'

    def calculate_cost(self):
        cost = self.cookie_quantity * self.price_per_dozen
        return cost

class IceCream(DessertItem):
    def __init__(self,name,scoop_count,price_per_scoop):
        super().__init__(name)
        self.scoop_count = scoop_count
        self.price_per_scoop = price_per_scoop
   
    def __str__(self):
        return f'{self.name}, {self.scoop_count} scoops, ${self.price_per_scoop}/scoop, ${self.calculate_cost}, {self.calculate_tax}'

    def calculate_cost(self):
        cost = self.scoop_count * self.price_per_scoop
        return cost

class Sundae(IceCream):
    def __init__(self,name,scoop_count,price_per_scoop,topping_name,topping_price):
        super().__init__(name,scoop_count,price_per_scoop)
        self.topping_name = topping_name
        self.topping_price = topping_price
    
    def __str__(self):
        return f'{self.name}, {self.scoop_count} scoops, ${self.price_per_scoop}/scoop, {self.topping_name}, ${self.topping_price}, ${self.calculate_cost}, {self.calculate_tax}'

    def calculate_cost(self):
        cost = (self.scoop_count * self.price_per_scoop)+(self.topping_price)
        return cost

class Order():
    def __init__(self):
        self.order = []

    def __len__(self):
        return len(self.order)

    def add(self,added_item):
        self.order.append(added_item)    

    def order_cost(self):
        total_cost = 0.00
        for i in self.order:
            total_cost += i.calculate_cost()
        return total_cost
    
    def order_tax(self):
        total_tax = 0.00
        for i in self.order:
            total_tax += i.calculate_tax()
        return round(total_tax)
