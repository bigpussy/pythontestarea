# -*- coding: utf-8 -*-
print u"类"
class Student(object):
	def __init__(self, name = 'Simpson', score = 85):
		self.name = name
		self.score = score
bart = Student()

print bart
#bart.name = 'Simpson'
print bart.name,bart.score
