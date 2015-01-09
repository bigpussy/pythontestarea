# -*- coding: utf-8 -*-
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
	
	__tablename__ = 'user'
	
	id = Column(String(20), primary_key=True)
	name = Column(String(20))

engine = create_engine('mysql+mysqlconnector://root:password@192.168.42.129:3306/test')

DBSession = sessionmaker(bind=engine)

session = DBSession()

user = session.query(User).filter(User.id=='1').one()

print 'type:' , type(user)
print 'name:', user.name 
session.close()
