# dictionaries 

alien_0 = {'color': 'green', 'points' : 5}
print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']

print(f"You just earned {new_points} points!")

print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)

alien_0 = {'color': 'green', 'points' : 5}
print(f"The alien has color {alien_0['color']} and has {alien_0['points']} points")

alien_0['color'] = 'yellow'
alien_0['points'] = 10
print(f"The alien has color {alien_0['color']} and has {alien_0['points']} points")

alien_0 = {'x' : 0, 'y' : 25, 'speed': 'medium'}
print(f"Current alien position: {alien_0['x']}")

if alien_0['speed'] == 'slow': 
    x_d = 1
elif alien_0['speed'] == 'medium': 
    x_d = 2
elif alien_0['speed'] == 'fast': 
    x_d = 3
    
point_value = alien_0.get('points', 'no points')
print(point_value)
    
alien_0['x'] = alien_0['x']  + x_d 
print(f"New alien position: {alien_0['x']}")

alien_0['speed'] == 'fast'

favourite_languages = {
    'jen' : 'python',
    'sarah': 'c',
    'michael': 'rust', 
    'samer': 'perl', 
    'hadrian' : 'python'
    }

language = favourite_languages['jen'].title()
print(f"Jen's favorite language is {language}")

for l,lang in favourite_languages.items(): 
    print(f"\n{l.title()} favorite programming language is {lang.title()}\n")
    
persons = {'first_name': 'Michael', 'last_name' : 'Zeppa', 'age': 31, 'city' : 'toronto'}
print(persons)

fave_num = {'Michael' : 22, 'Smaer' : 33}
for p, f in fave_num.items():
    print(f"\n{p.title()}'s favourite number is {f}.\n")

glossary = {'variable': 'a mutable and changeable value as defined by the user',
            'constant' : 'in immutable value', 
            'oop' : 'object-oriented programming',
            'tuples' : 'lists within lists. it is a kind of database'}
for g, definitions in glossary.items():
    print(f"\n{g.title()} means {definitions.title()}.\n")

user_names = {
    'username' : 'efermi', 
    'first' : 'enrico',
    'last' : 'fermi'
}

for key, value in user_names.items():
    print(f"Key: {key.title()}\n")
    print(f"Value: {value.title()}\n")
    
print(favourite_languages)

user_names = {
    'username' : 'efermi', 
    'first' : 'enrico',
    'last' : 'fermi'
}

glossary = {'variable': 'a mutable and changeable value as defined by the user',
            'constant' : 'in immutable value', 
            'oop' : 'object-oriented programming',
            'tuples' : 'lists within lists. it is a kind of database'}
for g, definitions in sorted(glossary.items()):    
    if g == 'oop': 
        print(f"\n{g.upper()} means {definitions.title()}.\n")
    else: 
        print(f"\n{g.title()} means {definitions.title()}.\n")
    
glossary = {'variable': 'a mutable and changeable value as defined by the user',
            'constant' : 'in immutable value', 
            'oop' : 'object-oriented programming',
            'tuples' : 'lists within lists. it is a kind of database'}
for g in glossary.keys():     
    if g == 'oop': 
        print(f"\n{g.upper()}.\n")
    else: 
        print(f"\n{g.title()}.\n")

glossary = {'variable': 'a mutable and changeable value as defined by the user',
            'constant' : 'in immutable value', 
            'oop' : 'object-oriented programming',
            'tuples' : 'lists within lists. it is a kind of database'}

for definitions in glossary.values(): 
    if g == 'oop': 
        print(f"\n{definitions.upper()}.\n")
    else: 
        print(f"\n{definitions.title()}.\n")

glossary = {'variable': 'a mutable and changeable value as defined by the user',
            'constant' : 'in immutable value', 
            'oop' : 'object-oriented programming',
            'tuples' : 'lists within lists. it is a kind of database',
            'loop' : 'either for or while loops are available in python',
            'class': 'a kind of data structure to store information', 
            'integer' : 'a whole number', 
            'list' : 'a data base with information, a key and a value'
            }
for g, definitions in sorted(glossary.items()):    
    if g == 'oop': 
        print(f"\n{g.upper()}: {definitions.title()}.\n")
    else: 
        print(f"\n{g.title()}: {definitions.title()}.\n")
        
rivers = {
    'nile' : 'egypt',
    'thames' : 'england', 
    'yellow river' : 'china'
    }

for r, c in rivers.items():
    print(f"The River {r.title()} is in {c.title()}.\n")
    
favourite_languages = {
    'jen' : 'python',
    'sarah': 'c',
    'michael': 'rust', 
    'samer': 'perl', 
    'hadrian' : 'python',
    'jie': 'java', 
    'brittany' : 'matlab'
    }

for l,lang in favourite_languages.items(): 
    print(f"\n{l.title()} favorite programming language is {lang.title()}\n")
    
if 'erin' not in favourite_languages.keys(): 
    print(f"Erin, plase take the favourite languages poll.")
    
alien_0 = {'color' : 'green', 'points' : 5}
alien_1 = {'color' : 'yellow', 'points' : 10}
alien_2 = {'color' : 'red', 'points' : 15}

aliens = [alien_0, alien_1, alien_2]

print(aliens)

for a in aliens: 
    print(a)
    
for a_num in range(30): 
    new_alien ={'color' : 'green', 'points' : 5, 'speed' : 'slow'}
    aliens.append(new_alien)
for a in aliens[:3]: 
    if a['color'] == 'green' : 
        a['color'] = 'yellow'
        a['speed'] = 'medium'
        a['points'] = 10
for a in aliens[:10]: 
    if a['color'] == 'green' : 
        a['color'] = 'red'
        a['speed'] = 'fast'
        a['points'] = 15
for a in aliens[:5]: 
    print(a)
print("...")

favourite_languages = {
    'jen' : ['python', 'ruby'], 
    'sarah' : ['c'],
    'edward': ['ruby', 'go'],
    'phil' : ['python', 'haskell']
}

for name, languages in favourite_languages.items(): 

    if languages == 1: 
        print(f"\n{name.title()}'s favourite languages is: ")
        for language in languages: 
            print(f"\t{language.title()}")
    else: 
        print(f"\n{name.title()}'s favourite languages are: ")
        for language in languages: 
            print(f"\t{language.title()}")

users = {
    'aeinstein' : {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton'
    }, 
    'mcurie' : {
        'first': 'marie', 
        'last': 'currie', 
        'location': 'paris'
    }
}

for username, user_info in users.items(): 
    print(f"username: {username}")
    full_name = f"{user_info['first'].title()} {user_info['last'].title()}"
    location = f"{user_info['location'].title()}"
    
    print(f"\tFull Name : {full_name}\nLocation : {location}\n")
    
person1 = {'first_name': 'Michael', 'last_name' : 'Zeppa', 'age': 31, 'city' : 'toronto'}    
person2 = {'first_name': 'Samer', 'last_name' : 'Harten', 'age': 31, 'city' : 'toronto'} 
person3 = {'first_name': 'Rebecca', 'last_name' : 'Wilson', 'age': 31, 'city' : 'toronto'}
person4 = {'first_name': 'Dewei', 'last_name' : 'Xu', 'age': 31, 'city' : 'mississauga'}  

people = [person1, person2, person3, person4]

print(people)

for p in people: 
    print(p)
    
pet1 = {'dog': 'xiong xiong'}
pet2 = {'dog' : 'monty'}

pets = [pet1, pet2]

for p in pets: 
    print(p)

f_places = {'Berlin', 'Niagara Falls', 'Toronto', 'Vancouver', 'Huan Shan'}

for fp in f_places: 
    print(fp)
    
fave_numbers = {'michael' : {11, 22}, 'samer' : {14, 24}} 

for f,n in fave_numbers.items(): 
    print(f)
    print(n) 

cities = {'Toronto': 'Canada', 'Washington, D.C.': 'United States of America'}

for c,countries in cities.items(): 
    print(c)
    print(countries)
    
