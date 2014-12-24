# -*- coding: utf-8 -*-
print u"类"
class Student(object):
	def __init__(self, name = 'Simpson', score = 85):
		self.__name = name
		self.__score = score
	def print_score(self):
		print '%s: %s' % (self.__name, self.__score)
	def get_grand(self):
		if self.__score >= 90:
			return 'A'
		elif self.__score >= 60:
			return 'B'
		else:
			return 'C'
	def get_name(self):
		return self.__name 
	def get_score(self):
		return self.__score 
	def set_score(self, score):
		if 0 <= score <= 100:
			self.__score = score
		else:
			raise ValueError('bad score')
bart = Student('Sara', 90)

print bart
#bart.name = 'Simpson' 
bart.print_score()
print bart.get_grand()
print bart.get_name()
bart.set_score(100)

print bart.get_score()
print bart._Student__score
