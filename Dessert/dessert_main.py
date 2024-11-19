from dessert_shop import DessertItem, Candy, Cookie, IceCream, Sundae

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