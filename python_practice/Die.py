import random
from random import randint
from random import choice

class Die:
    def __init__(self,sides):        
        self.sides = sides 
    def roll_die(self,sides):
        self.sides = sides
        number = randint(1,sides)
        print(f"The die rolled a number of {number}\n\n")
    def roll_multiple_instances(self,sides,instances):
        self.sides = sides
        self.instances = instances
        for i in range(1,instances): 
            value = self.roll_die(sides)
            print(f"The die rolled a value of {value}\n\n")
            
sides = 6
instances = 10
testDie = Die(sides)
testDie.roll_die(sides)
testDie.roll_multiple_instances(sides,instances)

sides = 10
instances = 20
testDie = Die(sides)
testDie.roll_die(sides)
testDie.roll_multiple_instances(sides,instances)

sides = 20
instances = 40
testDie = Die(sides)
testDie.roll_die(sides)
testDie.roll_multiple_instances(sides,instances)