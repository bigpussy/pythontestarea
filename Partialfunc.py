# -*- coding: utf-8 -*-
print u"偏函数"
print int('12345')
print u"可传入base参数"
print int('1111', base = 2)
print u"我们可以写一个只装换2进制的函数"
def int2(x , base = 2):
	return int(x , base)
print int2('100000')
print u"functools.partial就是帮助我们创建一个偏函数的"
import functools
int4 = functools.partial(int , base = 4)
print int4('12')
print int4('12',base = 5)