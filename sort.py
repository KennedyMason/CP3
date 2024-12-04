from operator import attrgetter

li = 9,1,8,2,7,3,6,4,5

slist = sorted(li)
slist1 = sorted(li, reverse=True)

"""
print(li)
print(slist)
print(slist1)
"""

dick = {"name" : "Tia", "job" : "Waterslide Tester", "age" : 28, "os" : "mac"}

sdick = sorted(dick)

class Employee:

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return "({}),({}),({})".format(self.name, self.age, self.salary )
    

e1 = Employee("Carl", 37, 70000)
e2 = Employee("Harry", 69, 0)
e3 = Employee("Me", 21, 7000000000000000000000000000000000000000)

employees = [e1, e2, e3]

def e_sort(emp):
    return emp.salary

semployees = sorted(employees, key = attrgetter('age'))

print(semployees)