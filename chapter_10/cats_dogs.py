

def read_animal_names(file_name):
    try:
        with open(file_name,'r') as f:
            lines = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {file_name} do not exist here in this directory")
        pass 
    except UnicodeDecodeError:
        pass 
    else:
        print(lines)

file_names = ['cats.txt', 'dogs.txt']
 
for file in file_names:
    read_animal_names(file)