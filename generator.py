# -*- coding: utf-8 -*-
print u"生成器"
L = [x * x for x in range(10)]
print L
g = (x * x for x in range(10))
print g
print g.next()
print "go on"

for n in g:
	print n
print u"斐波那契"
def fib(max):
	n, a, b = 0, 0, 1
	while n < max:
		print b
		a, b = b, a + b

		n = n + 1
fib(11)
print u"修改成为generator"
def fib(max):
	n, a, b = 0, 0, 1
	while n < max:
		yield b
		a, b = b, a + b

		n = n + 1
for n in fib(20):
	print n
print u"yield执行顺序"

def odd():
	print 'step1'
	yield 1
	print 'step2'
	yield 3
	print 'step3'
	yield 5
for n in odd():
	pass


