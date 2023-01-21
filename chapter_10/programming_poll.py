exit_status = False
file_name = 'program_poll.txt'
reason = input("Enter a reason you love programming: ")
with open(file_name, 'w') as f:
    f.write(reason + "\n")
exit_code = input("Continue to enter reasons? [Y/N]")
if exit_code.upper() == 'Y': 
    exit_status = True
    f.close()
elif exit_code.upper() == 'N':
    exit_status = False
while (exit_status == False):
    reason = input("Enter a reason you love programming: ")
with open(file_name, 'a') as f:
    f.write(reason + "\n")
exit_code = input("Continue to enter reasons? [Y/N]")
if exit_code.upper() == 'Y': 
    exit_status = True
    f.close()
elif exit_code.upper() == 'N':
    exit_status = False

with open(file_name, 'r') as f:
    lines = f.readlines()
    
for line in lines:
    print(line)
    
f.close()

