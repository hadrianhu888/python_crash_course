with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())
print(contents)

file_name = 'pi_digits.txt'

with open(file_name) as file_object:
    lines = file_object.readlines()
    
    for line in file_object:
        print(line)
        print(line.rstrip())

    for line in lines:
        print(line.rstrip())
        
pi_string = ''
for line in lines:
    pi_string += line.rstrip()
    
print(pi_string)
print(len(pi_string))

file_name = 'pi_million_digits.txt'

with open(file_name) as file_object:
    lines = file_object.readlines()
    pi_string = ''
    for line in lines:
        pi_string += line.rstrip()
        
print(f"{pi_string[:52]}...")
print(len(pi_string))

birthday = input("Enter your birthday, in the form of mmdddyy: ")
if birthday in pi_string:
    print("Your birthday, {birthday}, appears in the first million digits of pi\n\n")
else: 
    print("Your birthday does not appear in the first million digits of pi\n\n")