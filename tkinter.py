# -*- coding: utf-8 -*-
print u"条件判断"
age = 20
if age >= 18:
	print 'Your age is', age
	print 'adult'

print u"也可以加入else语句"
age = 3
if age >= 18:
	print 'Your age is', age
	print 'adult'
else:
	print 'Your age is', age
	print 'kid'
print u"也可以加入elif语句,更加判断详细"
age = 7
if age >= 18:
	print 'Your age is', age
	print 'adult'
elif age >= 6:
	print 'Your age is', age
	print 'teenager'
else:
	print 'Your age is', age
	print 'kid'


