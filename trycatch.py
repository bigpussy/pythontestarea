# -*- coding: utf-8 -*-
print u"错误处理"
import logging
try:
	print 'try...'
	r = 10 / int('0')
	print 'result:', r 
except StandardError, e:	
	logging.exception(e)
except ValueError, e:
	print 'ValueError:' , e 
except ZeroDivisionError, e:
	print 'except:', e 
else:
	print 'no error'
finally:
	print 'finally...'
print 'END'


