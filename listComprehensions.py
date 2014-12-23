# -*- coding: utf-8 -*-
print u"列表生成"
print range(1, 11)
print u"但是要生成[1x1,2x2,3x3,...,10x10]怎么办？"
print u"笨方法"
L = []
for x in range(1, 11):
	L.append(x * x)
print L
print u"也可以这样做"
print [x * x for x in range(1, 11)]
print u"for 循环后面还可以加入判断"
print [x * x for x in range(1, 20) if x % 2 ==0]
print u"还可以使用两层循环，可以生成全排列"
print [m + n + u for m in 'ABC' for n in 'XYZ' for u in 'QWE']
print u"运用列表生成式，可以写出很简洁的代码"
import os
print [d for d in os.listdir('.')]
d = {'x':'A', 'y':'B', 'z':'C'}
for k, v in d.iteritems():
	print k, '=', v
print [k + '=' + v for k, v in d.iteritems()]
print u"把list所有字符串变成小写"
L = ['Hello', ' World', 'IBM', 'Apple']
print [s.lower() for s in L]

L.insert(2,18)
print [s.lower() for s in L if isinstance(s, str)]
