prompt = "\nPlease enter a name of a city you have visited: "
prompt += "\nEnter 'quit' to exit.\n"

while True:
    city = input(prompt)
    if city == 'quit': 
        break
    else: 
        print(f"I'd love to go to {city.title()}")
        
