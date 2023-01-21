current_number = 0
while current_number < 10: 
    current_number += 1
    if current_number % 2 == 0: 
        continue
    print(current_number)

x = 1
while x <= 5:
    print(x)
    x += 1

x = 1
while x >= -10:
    print(x)
    x -= 1

pizza_toppings = input("Enter your pizza topping. Enter 'quit' to exit the program: ")

while pizza_toppings != 'quit':     
    if pizza_toppings == 'quit': 
        break; 
    else: 
        pizza_toppings = input(pizza_toppings)
        print(pizza_toppings)
        

