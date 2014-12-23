# -*- coding: utf-8 -*-
print u"迭代"
d = {'a':1, 'b':2, 'c':3}
for key in d:
	print key

for key,value in d.iteritems():	
	print key, ', ', value
print u"由于字符串也是对象"
for ch in 'ABC':
	print ch
print u"判断对象是否可以迭代"
from collections  import Iterable
print isinstance('abc', Iterable)
print isinstance([1, 2, 3], Iterable)
print isinstance(123, Iterable)
l = [1, 2, 3]
print len(l)
for i, value in enumerate(l):
	print i
l = [(1, 2), (2, 4), (3, 9)]
for x, y in l:
	print x, ':', y

	