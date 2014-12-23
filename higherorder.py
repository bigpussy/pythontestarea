# -*- coding: utf-8 -*-
print u"变量指向函数"
print abs
print u"函数赋值给变量"
f = abs
print f(-10)
print u"高阶函数"
def add(x, y, f):
	return f(x) + f(y)

print add(1 , -1 , f)

