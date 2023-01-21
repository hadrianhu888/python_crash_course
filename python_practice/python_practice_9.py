unconfirmed_users = ['alice', 'bob', 'candance', 'brian']
confirmed_users = []
while unconfirmed_users: 
    current_user = unconfirmed_users.pop()
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)
    print("\nThe following users have been confirmed: ")
    for confirmed_user in confirmed_users:
        print(confirmed_user)

pets = ['dog', 'cat', 'dog', 'goldfish', 'rabbit', 'cat']
print(pets)

while 'cat' in pets: 
    pets.remove('cat')
    
print(pets)