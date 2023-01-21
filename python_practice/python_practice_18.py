def make_album(artist, title):
    album = {}
    album = {'artist': artist, 'album title': title}
    return album 

a1 = make_album("mozart", "symphony number 5")
a2 = make_album("avril lavigne", "black star")
a3 = make_album("john williams", "star wars episode iii: the soundtrack")

print(a1)
print(a2)
print(a3)

while True: 
    print("\nPlease enter a musician and an album title: ")
    print(f"Please enter 'q' at any time to quit the program.")
    musician = input("Musician name: ")
    if musician == 'q': 
        break
    album_name = input("Album name: ")
    if album_name == 'q': 
        break
    
    formatted_name = make_album(musician, album_name)
    print(f"Musician and Album Names: {formatted_name}\n\n")

