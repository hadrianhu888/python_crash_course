read_file_name = 'file_to_write.txt'
    
with open(read_file_name) as f:
    lines = f.readlines()
    
for line in lines:
    print(line)
f.close()
