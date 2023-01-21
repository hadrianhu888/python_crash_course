import users
from users import User, Administrator, Privileges
privilege = ['can modify administration privileges']
testAdministrator = Administrator('first', 'last',privilege)
testAdministrator.__display_privileges__2__()
