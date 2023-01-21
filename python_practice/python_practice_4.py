prompt = "\bTell me something and I will repeat it back to you."
prompt += "\nEnter 'quit' to exit.\n"
message = ""
while message != 'quit':
    message = input(prompt)
    #print(message)
    
    if message != 'quit': 
        print(message)

