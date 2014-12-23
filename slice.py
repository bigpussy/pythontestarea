# -*- coding: utf-8 -*-
print u"切片"
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print u"笨方法"
print [L[0], L[1], L[2]]
print u"聪明点"
r = []
n = 3
for i in range(n):
	r.append(L[i])
print r
print u"最好用切片"
print L[0:3]
print u"还可以这样做"
print L[:3]
print L[2:5]
print u"切片很有用"
L = range(100)
print L
print L[:10]
print L[10:20]
print L[:10:2]
print L[2:20:5]
print L[1::5]
print range(100)[1::6]
print u"字符串也可以看成是list"[3:6]
print u"tuple 也是可以做切片的"
print (1, 2, 3, 4, 5, 6)[2:5]
