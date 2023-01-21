import Restaurant as rest 
from Restaurant import * 

name = 'yao ming'
cuisine = 'sea food'
customers = 100
seafood_restaurant = Restaurant(name,cuisine,customers)
seafood_restaurant.describe_restaurant(name,cuisine)

name1 = 'red lotus'
cuisine1 = 'chinese'
customers = 200
seafood_restaurant = Restaurant(name,cuisine,customers)
seafood_restaurant.describe_restaurant(name,cuisine)

name2 = 'green jasmine'
cuisine2 = 'tea'
customers = 400
seafood_restaurant = Restaurant(name,cuisine,customers)
seafood_restaurant.describe_restaurant(name,cuisine)


