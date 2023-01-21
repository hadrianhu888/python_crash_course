class Employee:
    def __init__(self,first,last,salary):
        self.first = first
        self.last = last
        self.salary = salary
    def give_raise(self):
        self.salary = self.salary + 5000
        print(f"New Salary is {self.salary}")
        return self.salary
    def give_custom_raise(self,amount):
        self.amount = amount
        self.salary = self.salary + self.amount
        print(f"New Salary is {self.salary}")
        return self.salary
    
