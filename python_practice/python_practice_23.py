def make_pizza(*toppings):
    print(toppings)

make_pizza('pepperoni')
make_pizza('pepperoni', 'extra cheese', 'basil', 'tomato', 'mushrooms')

def make_pizza_1(*toppings):
    print(f"Showing a summary of the pizza we are about to make: ")
    for top in toppings: 
        print(f" - {top.title()}")

make_pizza_1('pepperoni')
make_pizza_1('pepperoni', 'extra cheese', 'basil', 'tomato', 'mushrooms')

def make_pizza_2(size,*toppings): 
    print(f"Making a {size} inch pizza with the following toppings: ")
    for t in toppings: 
        print(f" - {t.title()}")


make_pizza_2('pepperoni')
make_pizza_2('pepperoni', 'extra cheese', 'basil', 'tomato', 'mushrooms')

def build_profile(first, last, **user_info): 
    user_info['first name'] = first
    user_info['last name'] = last
    return user_info

user_profile = build_profile('albert' ,'einstein', 
                             location = 'princeton',
                             field = 'physics')
print(user_profile)

def make_sandwiches (*sandwich_toppings): 
    print(f"The following are the desired toppings of the sandwich: ")
    print(f"{sandwich_toppings}")
    
make_sandwiches('tomato', 'bacon', 'cheese')

user = build_profile('hadrian', 
              'hu', 
              nationality = 'chinese', 
              location = 'hamilton', 
              favourite_movie = 'star wars')

print(user)

def make_car(manufacturer, model, **car_profile):
    car_profile['maker'] = manufacturer
    car_profile['model'] = model
    return car_profile

car = make_car('subaru', 'outback', color = 'blue', tow_package = True)
print(car)

