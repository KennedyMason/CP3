
class Pokemon:

    def __init__ (self, name, hp, typ, level):
        self.name = name
        self.hp = hp
        self.typ = typ
        self.level = level


    def __str__(self):

        return f"""Name:{self.name} 
Type: {self.typ}
Level: {self.level}
HP: {self.hp}
"""
    

    def combat(self, other):
        if self.level > other.level:
            return f"{self.name} won!"
        
        elif self.level < other.level:
            return f"{self.name} has been defeated!"
        
        elif self.level == other.level:
            return f"{self.name} and {other.name} are too exhausted ot fight. You both lose.\n"
        
    
    
    def level_up(self):
        self.level += 1
        self.hp *= int(self.hp*1.5)


    #Writing any method under @classmethod will keep themfrom changing object instances
    @classmethod

    def pikachu(self):
        return Pokemon(input("Give me a name: "), 50, "Electric", 1)


    #Static methods do not require self or cls
    @staticmethod
    
    def hp_update(poke):
        return poke.hp - 5
    




eevee = Pokemon("JayRod", 37, "Normal", 2)
charzard = Pokemon("Bob", 1, "Fire", 36)

pika = Pokemon.pikachu()
print(pika)

pika.hp = Pokemon.hp_update(pika)
print(pika)
