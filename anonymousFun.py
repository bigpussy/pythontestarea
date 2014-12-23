# -*- coding: utf-8 -*-
print u"匿名函数"
print map(lambda x:x * x, range(1,10))
f = lambda x: x * x 
print f
print f(5)
def build(x, y):
	return lambda: x * x + y * y 
f = build(2, 4)
print f()

