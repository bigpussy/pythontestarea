# -*- coding: utf-8 -*-
print u"装饰器"
def now():
	print '2013-12-25'
f = now 
f()
print now.__name__
print f.__name__
print u"decorator"
def log(func):
	def wrapper(*args, **kw):
		print 'call %s():' % func.__name__
		return func(*args, **kw)
	return wrapper

@log
def now():
	print '2013-12-25'
now()
print u"传送参数"
import functools
def log(text='decorator'):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args, **kw):
			print '%s %s():' %(text, func.__name__)
			return func(*args, **kw)
		return wrapper
	return decorator
@log('in the name of')
def now():
	print '2013-12-25'
now()
print now.__name__

print u"练习1"
def log(func):
	@functools.wraps(func)
	def decorator(*args, **kw):
		print 'begin call'
		func(*args, **kw)
		print 'end call'
	return decorator
@log
def now():
	print '20151515'
now()