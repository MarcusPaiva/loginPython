from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Column, ForeignKey, Integer, String, Table, DateTime, Float, Date, UniqueConstraint
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


db = create_engine( 'mysql://root:mypasswd@localhost/login' )
"""
Describe connection to database
"""

Base = declarative_base()

users = Table( 'users', MetaData( bind = None ) )
"""
Setting table
"""

class Connection:

	def connect( self ):
		"""
		Start connection with database
		"""
		Session = sessionmaker( bind = db )
		session = Session()
		return session

class Users( Base ):
	"""
	Describe columns in table Users
	"""
	__tablename__ = 'users'

	number = Column( Integer, primary_key = True )
	name = Column( String )
	password = Column( String )

	UniqueConstraint('name')
