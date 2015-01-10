# -*- coding: utf-8 -*-
print u"map函数"
def f(x):
	return x * x 

print map(f , [1, 2, 3, 4, 5, 6, 7, 8, 9])


print map(f , range(10))

print u"reduce函数"
def add(x , y):
	return x + y
print reduce(add , [1 , 2 , 3 , 4 , 5, 6])

def fn(x , y):
	return x * 10 + y
print reduce(fn , [1, 3, 5, 7, 9])
def char2num(s):
	return {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}[s]
print map(char2num, '13579')

print reduce(fn , map(char2num, '13579')) 

print u"整理为一个str2int函数"
def str2int(s):
	def fn(x , y):
		return x * 10 + y
	def char2num(s):
		return {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}[s]
	return reduce(fn , map(char2num, '13579')) 
print str2int('13579')
print u"lambda 函数"
g = lambda x:x * 2
print g(3)
def str2int(s):
	return reduce(lambda x, y : x * 10 + y, map(char2num, s))
print str2int("13579")
print u"练习1"
def cap(s):
	return s.capitalize()
print map(cap, ['adam', 'LISA', 'barT'])

print u"练习2"

def mutl(x , y):
	return x * y 
print reduce(mutl , range(1 , 10))
