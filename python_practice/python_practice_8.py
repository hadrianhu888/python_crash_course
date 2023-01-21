age = int(input("Enter your age: "))
if age < 3: 
    price = 0
if age < 12: 
    price = 10
if age >= 12: 
    price = 15
print(f"Your ticket price is : ${price:.2f}.")

