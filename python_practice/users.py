class User: 
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0
    def describe_user(self,first_name,last_name):
        title_style = f"First Name: {first_name}\n\nLast Name: {last_name}."
        print(title_style.title())
    def greeting(self,first_name, last_name):
        print(f"Hello {first_name.title()} {last_name.title()}")
    def increment_login_attempts(self,logins): 
        self.login_attempts += logins
        print(f"Login attempts: {self.login_attempts}")
    def rest_login_attempts(self):
        self.login_attempts = 0; 
        return self.login_attempts 
    
privileges_list = ['can add post', 'can delete post', 'can edit post', 'can add user', 'can remove user']

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
           
class Privileges(): 
    def __init__(self,privileges):
        self.privileges = privileges
    def show_privileges(self,p):
        for p in privileges_list:
            self.privileges = p
            print(self.privileges)

hadrian = User('hadrian', 'hu')
hadrian.describe_user('hadrian', 'hu')
hadrian.greeting('hadrian', 'hu')
hadrian.increment_login_attempts(1)

jiehu = User('jie','hu')
jiehu.describe_user('jie', 'hu')
jiehu.greeting('jie', 'hu')
jiehu.increment_login_attempts(1)

samer = User('samer', 'harten')
samer.describe_user('samer', 'harten')
samer.greeting('samer','harten')
samer.increment_login_attempts(1)
         
testAdministrator = Administrator('Administrator','One',privileges_list)
testAdministrator.__display_privileges__()

testPrivileges = Privileges('Administrator')
testPrivileges.show_privileges('can add posts')