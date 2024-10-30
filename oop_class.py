'''
OOP
how to create a class
what is class
what is object
attributes
initializing
instance
inheritance
methods
'''

class Animal:
    def sleep(self, name):
        self.name = name
        print(f'the {self.name} is sleeping')
        return self.name



dog = Animal()
dog.sleep('bulldog')

# A class is a collection of object or it can b defined as a prototype to create an object
# An object is an instance of a class


# class Employee:
#     '''
#     3 parameter name: location and salary
#     '''
#     bonus = 0.3
#     def __init__(self, name, location, salary):
#         self.name = name
#         self.location = location
#         self.salary = salary

#     def staff_detail(self):
#         detail = (f'my name is {self.name} and i am from {self.location}. my salary is {self.salary}')
#         return detail

#     def annual_bonus(self):
#         self.salary = self.salary * self.bonus
#         return self.salary
        

# emp1 = Employee('shalom', 'lagos', 10000)
# emp2 = Employee('joshua', 'niger', 5000)
# emp3 = Employee('teslim', 'oyo', 2000)

# emp1.name = 'shalom'
# emp1.location = 'lagos'
# emp1.salary = 10000

# emp2.name = 'joshua'
# emp2.location = 'niger'
# emp2.salary = 5000

# emp3.name = 'teslim'
# emp3.location = 'oyo'
# emp3.salary = 2000

# print('for emp1 details:', emp1.staff_detail())
# print('for emp2 details:', emp2.staff_detail())
# print('for emp1 bonus:', emp1.annual_bonus())
# print('for emp2 bonus:', emp2.annual_bonus())
# print('for emp3 bonus:', emp3.annual_bonus())

class StoreSale:
    bonus = 0.3
    def __init__(self, name, price, date, quantity, sale_rep):
        self.name = name
        self.price = price
        self.date = date
        self.quantity = quantity
        self.sale_rep = sale_rep

    def sales_report(self):
        self.total_cost = int(self.price) * int(self.quantity[0])
        report = (f'The product sold is {self.name} by {self.sale_rep}. The total price is {self.total_cost}')
        return report
    
    def give_bonus(self):
        give_b =  self.total_cost * self.bonus
        actual_b = self.total_cost - give_b

        return f'you have a bonus of {self.bonus} and the money you are paying is {actual_b}'


StoreSale1 = StoreSale('milo', '1800', '2024/08/4', '2 rolls', 'temi')
StoreSale2 = StoreSale('milk', '1400', '2024/08/4', '2 rolls', 'taiwo')

print(StoreSale1.sales_report())
print(StoreSale1.give_bonus())
print(StoreSale2.sales_report())
print(StoreSale2.give_bonus())

#remind her to teach us how to connect database to a class


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        Talk = (f'my name is {self.name}, i am {self.age} years old')
        return Talk
    
person1 = Person('temi', '15')
print(person1.talk())