
class Tech:

    def __init__(self, name, storage: int):
        self.name = name
        self.storage = storage


class Phone(Tech):

    def __init__(self, color):
        super()__init__()
        self.color = color

    def __str__(self):
        return f"A {self.color} {self.name} with {self.storage} storage."
    
    def __repr__(self):
        return f"Phone({self.name}, {self.storage}, {self.color})"
    

class Laptop(Phone):

    def __init__(self, size: int):
        super().__init__()
        self.size = size

    def __str__(self):
        return f"{self.size}-inch {self.name} with {self.storage} storage."
    
    def __repr__(self):
        return f"Laptop({self.name}, {self.storage}, {self.size})"
    
    
    





