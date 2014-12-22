# -*- coding: utf-8 -*-

print u"定义函数"
def my_abs(x):
	if not isinstance(x, (int, float)):
		raise TypeError('bad operand type')
	if x >= 0:
		return x
	else:
		return -x
print my_abs(100)
print my_abs(-20)
print my_abs(-12.34)
print u"参数类型检查"
#print my_abs('A')  # don't show this
print u"返回多个参数"
import math
def move(x, y, step, angle = 0):
	nx = x + step * math.cos(angle)
	ny = y - step * math.sin(angle)
	return nx, ny

x, y = move(100, 100, 60, math.pi / 6)
print x, y
print u"实际返回的是一个tuple"
print  move(100, 100, 60, math.pi / 6)