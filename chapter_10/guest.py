username = input("Enter your name: ")
filename = 'guest_file.txt'
with open(filename, 'w') as f:
    f.write(username)
f.close()
with open(filename, 'r') as f: 
    lines = f.readlines()    
for line in lines:
    print(line.title())
f.close()

