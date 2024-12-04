
from functools import reduce

mylist = [ 4, 6, 8, 1, 5, 10, 7,]
newlist = ["", "Argentina", "", "Brazil", "", "Colombia", "", "Chile"]

def increase(num):
    return num+1

#print(list(map(increase, mylist)))

def multiple(num):
    if num % 2 == 0:
        return num
    
#print(list(filter(multiple, mylist)))
#print(list(filter(lambda num: num % 3 == 0, mylist)))
#print(list(filter(None, newlist)))


multiplier = lambda x,y: x*y

print(reduce(multiplier, mylist))




