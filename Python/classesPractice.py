'''class Employee:
    pass
    creates an empty class
    classes are unique instances
    '''


class Employee:

    #Class variables are constant for each instance of class
    raise_amt = 1.04
    num_of_employees = 0
    
    #self is the individual instance of each class
    #__x__ is know as dunder, is a special method
    def __init__(self, first, last, pay):
        #These are instance Variables, per use
        self.first = first
        self.last = last
        self.pay = pay
        #Uses Employee cause there is no instance where you would want to change it for just one employee
        Employee.num_of_employees += 1

    #@propery treats the email mod like it was an attribute of Employee so you dont need to use ()
    @property
    def email(self):
        return "{}.{}@testcase.com".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


    #DO NOT FORGET SELF
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    #Decorator
    @classmethod
    #use cls instead of self for class methods
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount
        
    @classmethod
    #from is common for alternative constructers
    def from_string (cls, emp_str):
        #parces str 
        first, last, pay = emp_str.split('-')
        #Creates new employee
        return cls(first, last, pay)
    #static methods dont pass automatically, basically just a regular method. Just happens to be associated with the class    
    @staticmethod
    def is_workday(day):
        #checks if today is a work day, returns false if it is not. modays are 0 and sundays are 6
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
    #good method that should always be used, shows representation of class
    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay) 
    #used more for end users, takes priority over repr
    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)
    #adds the pay of two employees
    def __add__(self, other):
        return self.pay + other.pay
    #returns the length of an employees full name
    def __len__(self):
        return len(self.fullname())

#Inherits all of the atributes from Employee
class Developer(Employee):
    #does not effect parent classes amounts, pulls this value first
    raise_amt = 1.10
    #dont copy code from employee init method
    def __init__(self, first, last, pay, prog_lang):
        #passes first last and pay to the employee method
        super().__init__(first, last, pay)
        #another way to do this is
        #Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang
        
class Manager(Employee):
    
    def __init__(self, first, last, pay, subs=None):
        super().__init__(first, last, pay)
        if subs == None:
            self.subs = []
        else:
            self.subs = subs    
    #adds employees
    def add_subs(self, emp):
        if emp not in self.subs:
            self.subs.append(emp)
    #remove employees
    def remove_subs(self, emp):
        if emp in self.subs:
            self.subs.remove(emp)
    #prints employees under manager
    def print_emp(self):
        for emp in self.subs:
            print(emp)
emp_1 = Employee("Corey", "Schafer", 60000)
emp_2 = Employee("Dominic", "Lecluer", 40000)

'''emp_1.first = 'Corey'
emp_1.last = 'Schafer'
emp_1.email = 'corey.schafer@silverado.com'
emp_2.first = 'Dominic'
emp_2.last = 'Lecluer'
emp_2.email = 'Testemail'''

#Creats an instance variable for emp_1
emp_1.raise_amt = 1.05

Employee.set_raise_amt(1.06)

print(Employee.num_of_employees)
print(emp_1.email)
print(emp_2.last)
print(emp_2.email)
print(emp_2.fullname())
print(Employee.fullname(emp_1))
print(emp_1.raise_amt)
print(Employee.raise_amt)
#print(emp_1.__dict__)
#print(Employee.__dict__)

#Would have to split the string by - before use, so we make an alternative constructer
emp_str_1 = 'John-Doo-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

new_emp_1 = Employee.from_string(emp_str_1)
print(new_emp_1.__dict__)


import datetime
from pickle import INST
#checks todays date
my_date = datetime.date.today()

print(Employee.is_workday(my_date))
#prints out the info around the class Developer like resolution order and inherited methods
#print(help(Developer))

dev_1 = Developer('Test', 'User', 123456, "Python")
print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)

print(dev_1.prog_lang)

man_1 = Manager('Lisa', 'Taylor', 100000, ['Mike', 'Sarah'])    

print(man_1.subs)

man_1.print_emp()
man_1.add_subs("Josh")
man_1.remove_subs("Aaron")
man_1.print_emp()
#returns True, checks if it is under the umbrella of the class, same as issubclass
print(isinstance(man_1, Employee))
#returns string in the str or repr method
print(emp_1)
#Can call directly with 
print(emp_1.__repr__())

#int.__add__() is the same as using +, works with strings too with str.__add__() 
#calls upon the __add__ method to give the combined pay
print(emp_1 + dev_1)
#calls upon __len__ to return the length of an employees full name
print(len(emp_1))