class Restaurant:
    def __init__(self,name,cuisine_type,customers):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        self.customers = 0
    def describe_restaurant(self,name,cuisine_type):
        print(f"Restaurant name: {name.title()}")
        print(f"Cuisine Type: {cuisine_type.title()}")
    def count_served(self,customers):
        self.number_served += customers
        print(f"Customers served : {self.number_served}")
    def set_number_served(self,customers):
        self.customers = customers 
        print(self.customers)
    def increment_number_served(self,customers):
        customers = customers + 1
        self.customers = customers
        print(f"New number of customers: {self.customers}\n\n")    
name = 'yao ming'
cuisine = 'sea food'
customers = 55
seafood_restaurant = Restaurant(name,cuisine,customers)
seafood_restaurant.describe_restaurant(name,cuisine)
seafood_restaurant.count_served(12)

name1 = 'red lotus'
cuisine1 = 'chinese'
chinese_restaurant = Restaurant(name1,cuisine1,customers)
chinese_restaurant.describe_restaurant(name1,cuisine1)
chinese_restaurant.count_served(33)

name2 = 'green jasmine'
cuisine2 = 'tea'
tea_restaurant = Restaurant(name2,cuisine2,customers)
tea_restaurant.describe_restaurant(name2,cuisine2)
tea_restaurant.count_served(55)

