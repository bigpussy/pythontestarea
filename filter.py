# -*- coding: utf-8 -*-
print u"filter开始"
def is_odd(n):
	return n % 2 == 1
print filter(is_odd, range(1,15))

def not_empty(s):
	return s and s.strip()
print filter(not_empty, ['A','','B',None,'C', '  '])

print u"练习"
def isNum(num):
	if isinstance(num,int):
		return True
	else:
		return False
def isPrime(num):
	for i in range(2, num):
		if num % i == 0:
			return False
	return True
def isntPrime(num):
	return not isPrime(num)
print filter(isntPrime, range(2 , 100))
print u"stop"
