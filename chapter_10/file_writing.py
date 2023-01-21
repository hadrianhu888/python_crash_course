write_file_name = 'file_to_write.txt'
string_to_write = "I love programming.\n"

with open(write_file_name,'w') as f:
    f.write(string_to_write)
f.close()
    

