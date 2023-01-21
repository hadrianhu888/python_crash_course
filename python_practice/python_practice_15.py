def greet_user ():
    print("Hello")

greet_user()

def greet_user(username):
    print("Hello, " + username)
    
username = input("Enter your username: ")
greet_user(username)

def display_message(): 
    print("We are learning about functions in this chapter of Crash Course Python.")
    
display_message()

def favourite_book(title):
    print("Your favourite book is: " + title)

title = input("Enter a favourite novel or book: ")
favourite_book(title)

def describe_pet (animal_type, pet_name):
    """Display information about a pet"""
    print(f"I have an {animal_type.title()}.")
    print(f"The pet's name is {pet_name.title()}.")

describe_pet('golden retriever', 'xiong xiong')

describe_pet(animal_type = 'golden retriever', pet_name = 'xiong xiong')

def describe_pet (pet_name): 
    print(f"My pet's name is {pet_name.title()}")
    
describe_pet("xiong xiong")

def make_shirt(size,message):
    print(f"Shirt size: {size}")
    print(f"Message: {message.title()}")

make_shirt("large","Python is fun.")

def make_shirt(size,message):
    """Gets shirt size and desired shirt message"""
    size = "large"
    message = "I love Python"
    print(f"Shirt size: {size}")
    print(f"Message: {message.title()}")

make_shirt("large","Python is fun.")

def describe_city (city,country): 
    """describes a city and the country of the city"""
    print(f"{city.title()} is in {country.title()}.")

describe_city("toronto", "canada")

def get_formatted_name (first_name, last_name):
    """Return full name, neatly formatted"""
    print(f"Full Name: {first_name.title()} {last_name.title()}.")
    
get_formatted_name("hadrian", "hu")

def get_formatted_name (first_name, middle_name,last_name): 
    """Returns the full name with middle name as an option."""
    if middle_name: 
        full_name = f"Full Name: {first_name.title()} {middle_name.title()} {last_name.title()}."
    else: 
        full_name = f"Full Name: {first_name.title()} {last_name.title()}."
    return full_name

musician = get_formatted_name("jimi", " ","hendrix")
print(musician)

musician1 = get_formatted_name("john", "hooker", "lee")
print(musician1)

def build_person(first_name, last_name, age=None): 
    """Return dictionary of information regarding a person"""
    person = {'first': first_name, 'last': last_name}
    if age: 
        person['age'] = age
    return person 
musician = build_person('jimi', 'hendrix')
print(musician)

def get_formatted_name (first_name, last_name):
    """Return full name, neatly formatted"""
    print(f"Full Name: {first_name.title()} {last_name.title()}.")
    
get_formatted_name("hadrian", "hu")

while True: 
    print("\nPlease tell me your name: ")
    print(f"Please enter 'q' at any time to quit the program.")
    f_name = input("First name: ")
    if f_name == 'q': 
        break
    l_name = input("Last name: ")
    if l_name == 'q': 
        break
    
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"Hello, {formatted_name}!")




    

