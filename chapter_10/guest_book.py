        
file_name = 'guest_book.txt' 
exit_status = False
guest_name = input('Enter your name: ')
with open(file_name, 'w') as f:
    f.write(guest_name + "\n")
exit_text = input("Leave the program? /[Y/N]")
if exit_text.upper() == 'Y':
    exit_status = True
    f.close()
elif exit_text.upper() == 'N': 
    exit_status = False
while (exit_status == False):
    guest_name = input('Enter your name: ')
    with open(file_name, 'a') as f:
        f.write(guest_name + "\n")
    exit_text = input("Leave the program? /[Y/N]")
    if exit_text.upper() == 'Y':
        exit_status = True
        exit()
    elif exit_text.upper() == 'N': 
        exit_status = False
    f.close()  
    
with open(file_name,'r') as f:
    lines = f.readlines()

for line in lines:
    print(line.title())
    
f.close()
    

    

        
