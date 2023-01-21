import json
from sqlite3 import DataError

numbers = [2,3,5,7,11,13]

file_name = 'numbers_practice.json'

with open(file_name,'w') as f:
    """write the content to the json file"""
    json.dump(numbers,f)
    
with open(file_name, 'r') as f:
    """print out the contents of the json file"""
    contents = json.load(f)
    
    
print(f"The contents of the json file, {file_name} are: \n\n")
print(contents)

user_name = input("What is your name? ")
file_name = 'user_name_storage.json'

with open(file_name,'w') as f:
    """print out the json file"""
    json.dump(user_name,f)
    print(f"We'll remember you when you come back, {user_name}\n\n")

with open(file_name, 'r') as f:
    json_contents = json.load(f)
    
print(f"The contents of {file_name} is: ")
print(json_contents)
print(f"Welcome back, {json_contents}")

def greet_user():
    """Greet the user and store username in a json file with exception handling"""
    file_name = 'user_name_json.json'
    try:
        with open(file_name,'r') as f:
            user_name = json.load(f)
    except FileNotFoundError:
        print(f"Sorry, the file, '{file_name}' is not present.\n\n")
        user_name = input("What is your name? ")
        with open(file_name, 'w') as f:
            json.dump(user_name, f)
            print(f"We will remember your user name, {user_name}\n\n")
    else:
        print(f"Welcome back, {user_name}")

greet_user()

def get_user_name():
    file_name = 'new_user.json'
    new_user_name = input("Enter your new user name: ")
    try:
        with open(file_name,'w') as f:
            json.dump(new_user_name, f)
    except FileNotFoundError:
        return None
    else:
        print(f"Your user name is: {new_user_name}")
        
def verify_user():
    """Greet the user and store username in a json file with exception handling"""
    file_name = 'user_name_json.json'
    try: 
        user_name = input("Is this the correct user name? [y/n]")
        if user_name.lower() == 'y':            
            try:
                with open(file_name,'r') as f:
                    user_name = json.load(f)
            except FileNotFoundError:
                print(f"Sorry, the file, '{file_name}' is not present.\n\n")
                user_name = input("What is your name? ")
                with open(file_name, 'w') as f:
                    json.dump(user_name, f)
                    print(f"We will remember your user name, {user_name}\n\n")
            else:
                print(f"Welcome back, {user_name}")
        elif user_name.lower() == 'n':
            get_user_name()
        else:
            return None 
    except ValueError:
        verify_user()
    else:
        print(f"Your user name is {user_name}\n\n")
        
verify_user()

