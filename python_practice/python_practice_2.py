#user inputs and while loops 

message = input("Tell me something, and I will repeat it back to you : ")
print(message)
print("You said " + "'" + message + "'")

name = input("Please enter your name: ")
print(f"Hello, {name.title()}")

prompt = "If you tell us who you are, we can personalize the message you see. "
prompt += "\nWhat is your name? "

name = input(prompt)
print(f"Hello, {name.title()}")

age = int(input("How old are you? "))
print(age)

age = int(age)
print(age >= 18)

