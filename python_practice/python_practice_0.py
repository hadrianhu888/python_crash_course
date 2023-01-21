#Hadrian 
#June 20, 2021

import this 
        
print("\n\nChapters 1 and 2 sections go here\n\n")

text = "Hello World!"
text1 = "Welcome to Python Interpreter!"

print(text)

print(text1)

message = "Hello Python world!"
print(message)

message1 = "Hello Python Crash Course world!"

print(message1)

message2 = "Hello Python Crash Course reader!"

print(message2)

name = "ada lovelace"

print(name.title())
print(name.upper())
print(name.lower())

firstname = "ada"
lastname = "lovelace"

print("Concantated strings: "
    + firstname 
    + " " 
    + lastname)

fullname = f"Hello, {firstname} {lastname}, {text1}"
print(fullname)

fullname = f"Hello, {firstname} {lastname}, {text1}"
print(fullname.title())

fullname = "{} {}".format(firstname, lastname)

print(fullname.title())

print("Python")
print("\tPython")
print("\nPython")

print("Languges: \nPython\nC\nJavaScript\n\n")

favourite_language = 'python'
print(favourite_language.title())

print(favourite_language.rstrip())

favourite_language = favourite_language.rstrip()
print(favourite_language)

favourite_language = favourite_language.lstrip()
print(favourite_language)

favourite_language = favourite_language.strip()
print(favourite_language)

message3 = "One of Python's strengths, is its diverse community."
print(message3)

name = "Hadrian"
print(f"Hello {name} - {message1}")
print(f"Hello {name.lower()} - {message1}")
print(f"Hello {name.upper()} - {message1}")
print(f"Hello {name.title()} - {message1}")

quote = "Albert Einstein once said that \"A person never made a mistake, never tried anything new.\" "

print(quote)

famous_person= "Albert Einstein"
quote = "A person never made a mistake, never tried anything new." 

new_quote = f"{famous_person} once said {quote}"

print(new_quote)

name ="\t\tHadrian\n\n"

print(name.lstrip())
print(name.rstrip())
print(name.strip())

x = 2+3
x0 = 3-2
x1 = 2*3
x2 = 3/2
x3 = 3**2
x4 = 3**3
x5 = 10**6
x6 = 2+3*4 
x7 = (2+3)*4

print(x)
print(x0)
print(x1)
print(x2)
print(x3)
print(x4)
print(x5)
print(x6)
print(x7)

f = 0.1+0.1
f0 = 0.2+0.2
f1 = 2*0.1
f2 = 2*0.2 +0
f3 = 0.2+0.1
f4 = 3*0.10

f5 = 4/2
f6 = 1+2.0
f7 = 3.0**2

print(f)
print(f0)
print(f1)
print(f2)
print(f3)
print(f4)

print(f5)
print(f6)
print(f7)

universe_age = 14_000_000_000
print(universe_age)

x,y,z = 0,0,0

print(f"{x}, {y}, {z}")

MAX_CONNECTIONS = 5000

print(MAX_CONNECTIONS)

print(4+4)
print(10-2)
print(32/4)
print(4*2)
print(2**3)
print(8//1)

fave_number = 33
print(f"Your favourite number is: {fave_number}.")

#say hello to everyone 

print("Hello Python, people!")

#lists start here 

print("\n\nChapter 3 section go here\n\n")

bicycles = ['trek', 'connondale', 'redline', 'specialized']
print(bicycles)

print(bicycles[0]) 

print(bicycles[0].title())

print(bicycles[1])
print(bicycles[3])

print(bicycles[-1])

message = f"My first bicycle was a {bicycles[0].title()}"
print(message)

friends = ["david", "samer", "michael", "rebecca", "brittany", "gong"]
for f in friends: 
    print(f.title())

for f in friends: 
    print(f"Hi there, {f.title()}.")

favourite_vehicles = ["tesla", "honda cv", "volkswagen gt"]
for fv in favourite_vehicles: 
    print(f"I like the vehicles in following order: {fv}, {fv.title()}")

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']

motorcycles = 'ducatii' 
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']

motorcycles.append('ducati')
print(motorcycles) 

motorcycles = ['honda', 'yamaha', 'suzuki']

del motorcycles[0]
print(motorcycles) 

motorcycles = ['honda', 'yamaha', 'suzuki']

popped_motorcyle = motorcycles.pop()
print(motorcycles)
print(popped_motorcyle)

motorcycles = ['honda', 'yamaha', 'suzuki']

popped_motorcyle = motorcycles.pop()
last_owned = motorcycles.pop()
print(f"The last motorcycle I owned is {last_owned.title()}.")
    
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned is {first_owned.title()}.")

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.remove('honda')
print(motorcycles)

guest_list = ['albert einstein', 'carl jung', 'heisenberg']
for gl in guest_list:
    print(f"Welcome {gl.title()} to my party!")

guest_list = ['albert einstein', 'carl jung', 'heisenberg']
print(guest_list)

guest_list = ['albert einstein', 'carl jung', 'heisenberg']

removed_guest = 'carl jung'
guest_list.remove(removed_guest)

for gl in guest_list:
    print(f"Welcome {gl.title()} to my party!")

guest_list.insert(1,'carl jung')
guest_list.insert(0,'sigmund freud')
guest_list.append('fourier')

print(guest_list)

new_guest_list = guest_list 

print(new_guest_list)

for ngl in new_guest_list:
    print(f"Welcome {ngl.title()} to my party.")
    
new_guest_list_1 = new_guest_list
for ngl_1 in new_guest_list_1: 
    print(f"I am sorry, {ngl_1.title()}, I can only invite two of you to the party.")
    

print(f"I am sorry {new_guest_list_1[4].title()}, you've been removed from the guest list")
new_guest_list_1.pop() 
print(f"I am sorry {new_guest_list_1[3].title()}, you've been removed from the guest list")
new_guest_list_1.pop()
print(f"I am sorry {new_guest_list_1[2].title()}, you've been removed from the guest list")
new_guest_list_1.pop()

print(new_guest_list_1)

for n in new_guest_list_1: 
    print(f"{n.title()} - you're invited to the party")

new_guest_list_2 = new_guest_list_1
print(new_guest_list_2)

del new_guest_list_2[-1]
del new_guest_list_2[0]

print(new_guest_list_2)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

print("Here is the original list: ")
print(cars)

print("Here is the sorte d list: ")
print(sorted(cars))

print("Here is the original list again: ")
print(cars)

cars.reverse()
print(cars)

print(len(cars))

world_locations = ['hadrians wall', 'paris', 'moscow', 'berlin', 'rome', 'milan']
print(world_locations)

print(sorted(world_locations))
print(world_locations)

world_locations.reverse()
print(world_locations)

world_locations.reverse()
print(world_locations)

world_locations.sort()
print(world_locations)

world_locations.sort(reverse=True)
print(world_locations)

guest_list_3 = ['albert einstein', 'carl jung'] 

for n in guest_list_3: 
    print(f"{n.title()} - you're invited to the party")

print(f"{len(guest_list_3)} people have been invited to the party.")

rivers = ['nile', 'tigres-euphrates', 'mississippi', 'amazon', 'yellow river']

print(rivers)
rivers.sort()
print(rivers)
rivers.sort(reverse=True)
print(rivers)
print(len(rivers))
rivers.reverse() 
print(rivers)
print(sorted(rivers))
for r in rivers: 
    print((r.title()).upper())
    
# list operations start here 
    
magicians = ['alice', 'david', 'carolina']
for magician in magicians: 
    print(magician)
    
magicians = ['alice', 'david', 'carolina']
for magician in magicians: 
    print(f"{magician.title()} has a great trick!")
    
magicians = ['alice', 'david', 'carolina']
for magician in magicians: 
    print(f"{magician.title()} has a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}")
    
print("Thank you everyone, that was a great magic show")

pizzas = ['pepperoni', 'hawaiian', 'deluxe']

for p in pizzas: 
    print(f"I like {p.title()}")
print("I like pizza very much. Pizza is very delicious and a lovely Italian and Western cuisine.")

animals = ['dog', 'cat', 'rabbits']
for a in animals: 
    print(a.title())
    print(f"A {a.title()} would be a great pet")
print("All of these animals would make for a great pet")

for i in range(1,5): 
    print(i)
    
for i in range(1,6): 
    print(i)

numbers = list(range(1,6))
print(numbers)

even_numbers = list(range(2,11,2))
print(even_numbers)

squares = []
for value in range(1,11): 
    square = value ** 2
    squares.append(square)
print(squares)

squares1 = []
for value in range(1,11): 
    squares1.append(value ** 2)
print(squares1)

digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits)) 
print(max(digits)) 
print(sum(digits)) 

square = [value ** 2 for value in range(1,11)]
print(square)

for i in range(1,21): 
    print(i)

million = []
for j in range(1,1_000_000+1): 
    million.append(j)
print(million)

print(min(million))
print(max(million))
print(sum(million))

odd = []
for i in range(1,20,2): 
    odd.append(i)
print(odd)

tuples = []
for j in range(3,30): 
    tuples.append(j*3)
print(tuples)

cubes = []
for c in range(0,11): 
    cubes.append(c**3)
print(cubes)

cube_comprehension = [c ** 3 for c in range(0,11)]
print(cube_comprehension)

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1:4])

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[:4])

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[2:])

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[-3:])

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three (3) playerse of my team: ")
for p in players[:3]: 
    print(p.title())

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My Favourite foods are: ")
print(my_foods)

print("\nMy friends favourite foods are: ")
print(friend_foods)

my_foods.append('canoli')
friend_foods.append('ice cream')

print("My Favourite foods are: ")
print(my_foods)

print("\nMy friends favourite foods are: ")
print(friend_foods)

players = ['charles', 'martina', 'michael', 'florence', 'eli', 'gabriel']
print("Here are the first three (3) playerse of my team: ")
for p in players[0:3]: 
    print(p.title())

players = ['charles', 'martina', 'michael', 'florence', 'eli', 'gabriel']
print("Here are the middle three (3) playerse of my team: ")
for p in players[1:4]: 
    print(p.title())
    
players = ['charles', 'martina', 'michael', 'florence', 'eli', 'gabriel']
print("Here are the last three (3) playerse of my team: ")
for p in players[-3:]: 
    print(p.title())

my_pizzas = ['pepperoni', 'hawaiian', 'deluxe', 'seafood']
friends_pizzas = my_pizzas

print(my_pizzas)
print(friends_pizzas)

my_pizzas = ['pepperoni', 'hawaiian', 'deluxe', 'seafood']

my_pizzas.append('pine apple')
friends_pizzas.append('tomato')

print(my_pizzas)
print(friends_pizzas)

print("\n\nMy pizzas are: \n\n")

for p in my_pizzas: 
    print (p.title())
    
print("\n\nFriends' pizzas are: \n\n")

for q in friends_pizzas: 
    print(q.title())

## tuples start here 

dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])

dimensions = (200,50)
#dimensions[0] = 250

print(dimensions[0])
print(dimensions[1])

for d in dimensions: 
    print(d)
    
print("Original dimensions: ")
for d in dimensions: 
    print(d)

dimensions = (400,100)
print("New dimension: ")
for d in dimensions: 
    print(d) 

buffet = ("Shrimp", "Crab", "Beaf", "Veal", "Goat Milk")
for b in buffet: 
    print(b)

# buffet[0] = "Lobster" - error message here 

buffet = ("Shrimp", "Crab", "Beaf", "Shark", "Lobster")
for b in buffet: 
    print(b)
    
## conditional statements start here 

cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw': 
        print(car.upper())
    else: 
        print(car.title())
        
car = 'bmw'
print(car == 'bmw')

car = 'audi'
print(car == 'bmw')

car = 'Audi'
print(car == 'audi')

car = 'Audi'
print(car.lower() == 'audi') 

print(car)

requested_topping = 'mushrooms'
if requested_topping != 'anchovies': 
    print("Hold the anchovies!")

age = 18
print(age == 18)

answer = 17
print(answer != 42)

age = 19
print(age < 21) 
print(age <= 21)
print(age > 21)
print(age >= 21)

age_0 = 22
age_1 = 18
print (age_0 > age_1)

age_1 = 22

print(age_0 >= 21 and age_1 >= 21)

age_0 = 22
age_1 = 18
print(age_0 >= 21 or age_1 >= 21)

age_0 = 18 

print(age_0 >= 21 or age_1 >= 21)

requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)
print('pepperoni' in requested_toppings)

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users: 
    print(f"{user.title()}, you can post a response if you wish")
    
game_active = True 
can_edit = False 

car = 'honda civic'
print("True is expected")
print(car=='honda civic')
print("False is expected")
print(car == 'audi')
cars = ['Honda Civic', 'Tesla', 'BMW', 'Mercedes Benz'] 
print("True is expected")
print(cars[0].lower()== 'honda civic')
print("False is expected")
print(cars[0].upper()== 'honda civic')
print("True is expected")
print(2 >= 0 and 2 != 0)
print("False is expected")
print(0 >= 4 or cars[0] == 'audi')
print("False is expected")
print('leaf' in cars)
print("True is expected")
print('BMW' in cars)

age = 19
if (age >= 18): 
    print("You are qualified to vote!")
    print("Have you registed to vote yet? ")
    
age = 17
if (age >= 18): 
    print("You are qualified to vote!")
    print("Have you registed to vote yet? ")
else: 
    print("Sorry, you are too young to vote")
    print("Plesae register to vote as soon as you turn 18")

age = 12 
if age < 4: 
    print("Your admission cost is $0.00")
elif age < 18: 
    print("Your admission cost is $25.00")
else: 
    print("Your admission cost is $40.00")

age = 12
if age < 4: 
    price = 0
elif age < 18: 
    price = 25
else: 
    price = 40

print(f"Your admission cost is ${price:.2f}.")

requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings: 
    print("Adding mushrooms")
if 'pepperoni' in requested_toppings: 
    print("Adding pepperoni")
if 'extra cheese' in requested_toppings: 
    print("Adding extra cheese")

print("\nFinished making your pizza!")

alien_color ='green'
score = 0
if alien_color =='green': 
    score = score + 5
    print(f"Your score: {score}")
elif alien_color == 'yellow': 
    score = score + 10
    print(f"Your score: {score}")
elif alien_color == 'red': 
    score = score + 15
    print(f"Your score: {score}")
else: 
    score = score + 0
    print(f"Your score: {score}")

age = 33
if age < 2: 
    print("Infant")
elif age < 4: 
    print("Toddler")
elif age < 13: 
    print("Kid")
elif age < 20: 
    print("Teenager")
elif age < 65: 
    print("Adult")
else: 
    print("Elder")
    
favourite_fruits = ['apple', 'strawberry', 'grapes']
if 'grapes' in favourite_fruits: 
    print("You really like grapes!")
if 'strawberry' in favourite_fruits: 
    print("You really like strawbery")
if 'apple' in favourite_fruits: 
    print("You really like apples")
if 'banana' in favourite_fruits: 
    print("You really like bananas")
if 'blueberries' in favourite_fruits: 
    print("You really like blueberries")

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings: 
    print(f"Adding {requested_topping}")
print("Finished your pizza")

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings: 
    if requested_topping == 'green pepper': 
        print(f"Sory, we are out of {requested_toppings[1].title()}")
    else: 
        print(f"Adding {requested_topping}")
print("Finished your pizza")

requested_toppings = []

if requested_toppings: 
        for requested_topping in requested_toppings: 
            if requested_topping == 'green pepper': 
                print(f"Sory, we are out of {requested_toppings[1].title()}")
            else: 
                print(f"Adding {requested_topping}")
        print("Finished your pizza")
else: 
    print("Are you sure you want a plain pizza?")
    
usernames = ['admin', 'hadrian', 'guest', 'joyce', 'jack']
for u in usernames: 
    if u == 'admin': 
        print(f"Hello {u.title()}, would you like a status report?")
    else: 
        print(f"Hello {u.title()}!")

usernames = []
if usernames: 
    for u in usernames: 
        if u == 'admin': 
            print(f"Hello {u.title()}, would you like a status report?")
        else: 
            print(f"Hello {u.title()}!")
else: 
    print("We need to find some users!")

user_names = ['adam', 'alice', 'beatrice', 'jerome', 'jeremiah']
new_users = ['adam', 'alice', 'eve', 'rehnuba', 'berlin']

for i in range(0,5): 
    if new_users[i] == user_names[i]: 
        print(f"Please select a new username, since the username, {user_names[i]} is already taken.")
    elif new_users[i] != user_names[i]: 
        print(f"The user name {new_users[i]} is not taken.")

numbers = [1,2,3,4,5,6,7,8,9]
for i in range(1,10): 
    if i == 1: 
        print(f"{i}st")
    elif i == 2: 
        print(f"{i}nd")
    elif i ==3: 
        print(f"{i}rd")
    else: 
        print(f"{i}th")
    