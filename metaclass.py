# -*- coding: utf-8 -*-
def fn(self, name='world'):
	print('Hello, %s.' % name)

Hello = type('Hello',(object,), dict(hello=fn))

h = Hello()
h.hello()
print(type(Hello))
print(type(h))

print u"metaclass 演示"
class ListMetaclass(type):
	def __new__(cls, name, base, attrs):
		attrs['add'] = lambda self, value: self.append(value)
		return type.__new__(cls, name, base, attrs)
		
class MyList(list):
	__metaclass__ = ListMetaclass 

L = MyList()
L.add(1)
print L
	