file_name = 'what_i_learnt.txt'
first_language = 'Python'
second_language = 'C'

with open(file_name) as file_object:
    lines = file_object.readlines()
    for line in lines:    
        newline = line.replace(first_language, second_language)
        print(newline)

