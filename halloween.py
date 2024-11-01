from abc import ABC, abstractmethod
import random

class Monster(ABC): 

    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def attack_method(self):
        pass


class Zombie(Monster):
    
    def __init__(self, name):
        super().__init__(name)
        self.damage = random.randint(1, 100)
    
    def attack_method(self):
        return f"{self.name.title()} The Zombie rips out and eats the opponent's brain! It deals\n\
{self.damage} damage.\n"
    

class HeadlessHorseman(Monster):

    def __init__(self, name):
            super().__init__(name)
            self.damage = random.randint(1, 100)

    def attack_method(self):
        return f"{self.name.title()} The Headless Horseman hurls it's head at the opponent!\n\
It deals {self.damage} damage.\n"


class Spider(Monster):

    def __init__(self, name):
        super().__init__(name)
        self.damage = random.randint(1, 100)
    
    def attack_method(self):
        

        return f"{self.name.title()} The Spider bite the opponent, turning them into Spiderman!\n\
With this new power, the opponent is now responsible! It deals {self.damage} damage.\n"


class UrMom(Monster):

    def __init__(self, name):
        super().__init__(name)
        self.damage = random.randint(1, 1000)

    def attack_method(self):
        return f"{self.name.title()}, your mom, verbally reprimands the opponent! It deals\n\
{self.damage} damage.\n"
        
    

class Battle:

    def __init__(self, opp1, opp2):
        self.opp1 = opp1
        self.opp2 = opp2

    def fight(self):
        print(f"{self.opp1.name} fights {self.opp2.name}!\n")
        print(self.opp1.attack_method())
        print(self.opp2.attack_method())

        if self.opp1.damage > self.opp2.damage:
            print(f"{self.opp1.name.title()} wins!")

        if self.opp2.damage > self.opp1.damage:
            print(f"{self.opp2.name.title()} wins!")

        if self.opp1.damage == self.opp2.damage:
            print("It'a a tie!")


    


def pick_monster():

    monster_choice = input("Pick a monster: \n\
a. Zombie\n\
b. Headless Horseman\n\
c. Spider\n\
d. Your Mom\n")
    
    if monster_choice.lower() == "a":

        name = input("What's it's name?: ")
        

