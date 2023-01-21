print("Enter two numbers and I'll add them")
while True: 
    first_number = input("Enter first number: ")
    if first_number == 'q':
        break
    second_number = input("Enter second number: ")
    if second_number == 'q':
        break
    try: 
        sum = int(first_number) + int(second_number)
    except ValueError:
        print("Cannot add characters!")
    else:
        print(f"The sum of {first_number} and {second_number} is {sum}\n\n")
    
    
    