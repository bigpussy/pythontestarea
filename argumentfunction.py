# -*- coding: utf-8 -*-

print u"函数的参数"

def power(x, n = 2): 
	s = 1
	while n > 0:
		n = n - 1
		s = s * x 
	return s

print power(5)
print power(15)
print power(15, 3)

print u"坑"
def add_end(L=[]):
	L.append('END')
	return L

print add_end([1, 2, 3,])
print add_end()
print add_end()
print add_end()
print u"不坑了"
def add_end(L=None):
	if L is None:
		L = []
	L.append('END')
	return L
print add_end()
print add_end()
print add_end()
print u"可变参数"
def calc(*numbers):
	sum = 0
	for n in numbers:
		sum = sum + n * n
	return sum
print calc(1,2,3)
print u"关键字参数"
def person(name, age, **kw):
	print 'name', name, 'age:', age, 'other:', kw
	
person('Michael', 30)
person('Bob', 35, city='Beijing')
person('Adam', 45, gender='M', job='Engineer')
kw = {'city':'Beijing', 'job':'Engineer'}
person('Jack', 24, **kw)

print u"参数顺序"

def func(a, b, c = 0, *args, **kw):
	print 'a=', a, 'b=', b, 'c=', c, 'args=', args, 'kw', kw
func(1, 2)
func(1, 2, 3, )
func(b = 2, a = 1)
func(1, 2, 3, 4)
func(1, 2, 3, 4, 5)
func(1, 2, 3, 4, 5, x = 99)

args = (1, 2, 3, 4)
kw = {'x':99}
func(*args, **kw)