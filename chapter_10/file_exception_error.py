import unicodedata 

file_name = 'alice.txt'

def count_words(file_name): 
    try: 
        """Try to open the file"""
        with open(file_name, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print("File not found!")
    except UnicodeDecodeError:
        print("Unicode decoding error!")
    else:
        """Print the text in the file"""
        words = contents.split()
        num_words = len(words)
        print(f"The file {file_name} has {num_words} words\n\n")
 
file_name1 = 'little_women.txt'
file_names = ['alice.txt', 'little_women.txt', 'moby_dick.txt']

for files in file_names:
    count_words(files)

def count_word(file_name, word): 
    try: 
        """Try to open the file"""
        with open(file_name, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print("File not found!")
    except UnicodeDecodeError:
        print("Unicode decoding error!")
    else:
        """Print the text in the file"""
        words = contents.split()
        word_count = contents.count(word)
        num_words = len(words)
        print(f"The file {file_name} has {num_words} words\n\n")
        print(f"The file {file_name} has {word_count} words containing the word '{word}'\n\n")

file_names = ['alice.txt', 'little_women.txt', 'moby_dick.txt']
word = 'the '
alternate_word = 'the'
for files in file_names:
    count_word(files,word)

for files in file_names:
    count_word(files,alternate_word)

