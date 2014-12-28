# -*- coding: utf-8 -*-
print u"调试"
def foo(s):
	n = int(s)
	print '>>> n = %d' % n 
	assert n != 0, 'n is zero'
	return
def main():
	foo('1')


main()


