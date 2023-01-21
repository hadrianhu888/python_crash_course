def make_pizza(*toppings):
    print(toppings)

make_pizza('pepperoni')
make_pizza('pepperoni', 'extra cheese', 'basil', 'tomato', 'mushrooms')

def make_pizza(*toppings):
    print(f"Showing a summary of the pizza we are about to make: ")
    for top in toppings: 
        print(f" - {top.title()}")

make_pizza('pepperoni')
make_pizza('pepperoni', 'extra cheese', 'basil', 'tomato', 'mushrooms')

def make_pizza(size,*toppings): 
    print(f"Making a {size} inch pizza with the following toppings: ")
    for t in toppings: 
        print(f" - {t.title()}")


make_pizza('pepperoni')
make_pizza('pepperoni', 'extra cheese', 'basil', 'tomato', 'mushrooms')

def build_profile(first, last, **user_info): 
    user_info['first name'] = first
    user_info['last name'] = last
    return user_info

user_profile = build_profile('albert' ,'einstein', 
                             location = 'princeton',
                             field = 'physics')
print(user_profile)

