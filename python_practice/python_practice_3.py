print(4%3)
print(5%3)
print(6%3)
print(7%3)

number = input("Enter a number, and I'll tell yu if it is even or odd: ")
number = int(number)

if number % 2 == 0: 
    print(f"{number}: Even")
else: 
    print(f"{number}: Odd")
    
RentalCar = input("Please enter the kind of rental car you would like: ")
print(f"Let me see if I can find {RentalCar} in our inventory.\n\n")

DinnerGuests = int(input("How many guests are attending your party? "))
if DinnerGuests >= 8: 
    print(f"You will have to wait, since you have {DinnerGuests} guests.")
elif DinnerGuests > 0 and DinnerGuests < 8: 
    print(f"You can go into the seating area, since you have {DinnerGuests} guests.")
    
userNumber = int(input("Enter a number: "))
if userNumber % 10 == 0: 
    print(f"{userNumber} is a multiple of 10.")
else: 
    print(f"{userNumber} is not a multiple of 10.")
    
current_number = 1

while current_number <= 5: 
    print(current_number)
    current_number += 1
    

