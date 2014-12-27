# -*- coding: utf-8 -*-
print u"定製類"

class Student(object):
	def __init__(self, name):
		self._name = name
	def __str__(self):
		return 'Student object (name:%s)' % self._name
	def __getattr__(self, attr):
		if attr=='age':
			return lambda: 25
		raise AttributeError('\'Student\' object has no attribute \' %s \'' % attr)
	def __call__(self, age=10):
		print('My name is %s. My age is %s' % (self._name, age))

print Student('Michael')

s = Student('Michael')
print s

class Fib(object):
	def __init__(self):
		self.a , self.b = 0 , 1
	
	def __iter__(self):
		return self
	def next(self):
		self.a , self.b = self.b , self.a + self.b
		if self.a > 100000:
			raise StopIteration();
		return self.a
	def __getitem__(self , n):
			if isinstance(n , int):
				a , b = 1 , 1
				for x in range(n):
					a , b = b , a + b
				return a
			if isinstance(n , slice):
				start = n.start
				stop = n.stop
				a , b = 1 , 1
				L = []
				for x in range(stop):
					if x >= start:
						L.append(a)
					a , b = b , a + b 
				return L
for n in Fib():
	print n
print Fib()[9]
print "slice"
print Fib()[0:10]
print u"不存在的属性"
print s.age()


print u"链式调用"
class Chain(object):
	def __init__(self, path = ''):
		self._path = path 
	def __getattr__(self, path):
		return Chain('%s/%s' % (self._path, path))
	def __str__(self):
		return self._path

print Chain().status.user.timeline.list

print u"直接对实例进行调用"

s(20)

print callable(s)
print callable(Student)
Student('Michael')(20)
