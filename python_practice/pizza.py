def make_pizza(size,*toppings): 
    print(f"Making a {size} inch pizza with the following toppings: ")
    for t in toppings: 
        print(f" - {t.title()}")
        
        