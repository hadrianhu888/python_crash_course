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