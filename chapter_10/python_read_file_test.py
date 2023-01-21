file_name = 'what_i_learnt.txt'
try:     
    with open(file_name) as file_object:
        """Open and read the file"""       
except FileNotFoundError:
    pass 
else:
    file_object.read()
try: 
    with open(file_name) as file_object:
        lines = file_object.readlines()
    for line in lines:
        print(line)
except FileNotFoundError:
    pass 
else:
    pass 

with open(file_name) as file_object:
    lines = file_object.readlines()
    for line in lines:
        line.replace('Python', 'C')
    print(lines)
     
string_text = ''   
with open(file_name) as file_object: 
    lines = file_object.readlines() 
    for line in lines:
        string_text += line.rstrip()        
print(string_text)  

with open(file_name) as file_object:
    lines = file_object.readlines()
    for line in lines:    
        line.replace('Python', 'C')
        print(line)