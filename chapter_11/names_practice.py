import name_function_practice 
from name_function_practice import *
print("Enter 'q' at any time to quit.")
while True:
    first = input("Enter your first name: ")
    if first == 'q':
        break
    last = input("Enter your last name: ")
    if last == 'q':
        break    
    formatted_name = get_formatted_name_practice(first, last)
    print(f"\tNeatly formatted name: {formatted_name}\n\n")
    
