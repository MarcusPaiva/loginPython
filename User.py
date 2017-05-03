

class User:
	"""
	Represent characteristics of the user
	"""
	name = None
	password = None

	def getName( self ):
		return self.name

	def setName( self, name = None ):
		self.name = name

	def getPassword( self ):
		return self.password

	def setPassword( self, password = None ):
		self.password = password

