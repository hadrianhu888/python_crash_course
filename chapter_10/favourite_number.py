import json

def get_favorite_number():
    file_name = 'favorite_number.json'
    try:
        with open(file_name, 'r') as f:
            contents = json.load(f)            
    except FileNotFoundError:
        favorite_number = input("What is your favorite number? ")
        with open(file_name,'w') as f:
            json.dump(favorite_number,f)
    else:
        print(f"Your favorite number is: {contents}\n\n")

get_favorite_number()
get_favorite_number()
