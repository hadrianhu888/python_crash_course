import json

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