import Restaurant 
from Restaurant import Restaurant

name = 'golden pavilion'
cuisine = 'beijing duck'
initial_customers = 0
customers = 66
restaurant1 = Restaurant(name,cuisine,initial_customers)
restaurant1.describe_restaurant(name,cuisine)
restaurant1.count_served(customers)
restaurant1.increment_number_served(customers)
