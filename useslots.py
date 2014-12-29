# -*- coding: utf-8 -*-
print u"使用slot"
class Student(object):
	__slots__ = ('age', 'name' ,'set_age')
	pass
s = Student()
s.name = 'Michael'
print s.name

def set_age(self, age):
	self.age = age

from types import MethodType
s.set_age = MethodType(set_age, s , Student)
s.set_age(25)
print s.age



