from User import *
from orm import *
import hashlib

connection = Connection()
userTable = Users()
user = User()
"""
Instance the classes
"""

password = hashlib.md5( "myPassword" )
"""
Set encryption MD5 in password
"""

user.setName( "user" )
user.setPassword( password.hexdigest() )
"""
Set attributs to class User
"""

session = connection.connect()
"""
Start session from sql
"""

userTable.name = user.getName()
userTable.password = user.getPassword()
"""
Get attribute from class User
"""

session.add(userTable)
"""
Insert name and password into database
"""

session.commit()
"""
Commit database
"""

numberRows = session.query(Users).filter_by( name = user.getName(), password = user.getPassword() ).count()
"""
Count Rows where fields name and password are equals to Class User into database
"""

if numberRows == 1:
	"""
	If the numberRows is equal 1 grant access
	"""
	print "Grant access"

else:
	"""
	Else Deny access
	"""
	print "Denied"

