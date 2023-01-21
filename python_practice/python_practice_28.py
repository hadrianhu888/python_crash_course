import User 
import Admin
from User import User
from Admin import Administrator, Privileges
privilege = ['can modify administration privileges']
testAdministrator = Administrator('first', 'last',privilege)
testAdministrator.__display_privileges__2__()