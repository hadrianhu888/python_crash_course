print( "Give me two numbers, and I'll divide them.\n\n")
print ("Enter 'q' to quit.\n\n")

while True:
    first_number = input("\nEnter the first number:")    
    if first_number == 'q':
        break
    second_number = input("\nEnter the second number: ")
    if second_number == 'q':
        break
    try:
        quotient = int (first_number) / int (second_number)
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    else:
        print(f"The answer is {quotient}\n\n")
    
    
    