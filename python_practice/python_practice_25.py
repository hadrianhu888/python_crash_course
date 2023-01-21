import users
from users import User

class Administrator(User):
    privileges = ['can add post', 'can delete post', 'can edit post', 'can add user', 'can remove user']
    def __init__(self):
        return self.privileges
    def __display_privileges__(self,privileges):
        for p in privileges:
            print(self.privileges[p])
            
testAdministrator = Administrator.__display_privileges__
testAdministrator.__name__ = 'testAdministrator'



