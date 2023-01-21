from random import randint
from random import choice

test_rand = randint(1,6)
print(test_rand)

players = ['charles', 'martina', 'michael', 'florence', 'eli']
first_up = choice(players)
print(first_up.capitalize())
