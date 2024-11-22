from dessert_shop import DessertItem, Candy, Cookie, IceCream, Sundae

# class that makes order
class Order:

    def __init__(self, order = []):
        self.order = order

    def __str__(self):
        for item in self.order:
            print(f"{item.name}")
        
    def add(self, item):
        self.order.append(item)
      
    def total_items(self):
        total = len(self.order)
        return total
    
    def order_total(self):
        total = 0

        for item in self.order:
                total += item.calculate_cost()

        return round(total, 2)
    
    def order_tax(self):
        tax = 0
        for item in self.order:
            item_tax = item.calculate_tax(item.calculate_cost())
            tax += item_tax/100
        
        return round(tax, 2)
        


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
    print(f'Your total is ${order.order_total()}.')
    print(f'Your tax is ${order.order_tax()}.')
 
main()