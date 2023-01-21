import User 
from User import User

privileges_list = ['can add post', 'can delete post', 'can edit post', 'can add user', 'can remove user']

class Privileges(): 
    def __init__(self,privileges):
        self.privileges = privileges
    def show_privileges(self,p):
        for p in privileges_list:
            self.privileges = p
            print(self.privileges)

class Administrator(User):
    
    def __init__(self, first_name, last_name, privileges):
        self.first_name = first_name
        self.last_name = last_name
        self.privileges = privileges
    def __display_privileges__(self):
        for p in privileges_list:
           self.privileges = p
           print(p)
    def __display_privileges__2__(self):
        p = Privileges('can modify posts')
        p.show_privileges(p)