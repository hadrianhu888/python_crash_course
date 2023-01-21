responses = {}
polling_active = True 

while polling_active:
    name = input("\nWhat is your name? >>>> ")
    respnse = input("Which mountain would you like to climb today? >>>> ")
    responses[name] = respnse
    repeat = input("Would you like another person to respond? >>>> ")
    if repeat == 'no': 
        polling_active = False
print("Polling Results")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")


