# -*- coding: utf-8 -*-
print u"使用装饰器"
class Student(object):
	@property
	def get_score(self):
		return self._score
	@get_score.setter
	def set_score(self,value):
		if not isinstance(value , int ):
			raise ValueError('score must be an interger!')
		if value < 0 or value > 100:
			raise ValueError('score must between 0 ~ 100')
		self._score = value
	@property
	def birth(self):
		return self._birth
	@birth.setter
	def birth(self, value):
		self._birth = value
	@property
	def age(self):
		return 2014 - self._birth
s = Student()
s.set_score = 60
#print s.get_score()
print s.get_score


s.birth = 1984
print s.birth
print s.age


