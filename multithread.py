# -*- coding: utf-8 -*-
print u"多线程"

import time, threading

def loop():
	print 'thread %s is running...\n' % threading.current_thread().name
	n = 0 
	while n < 5:
		n = n + 1
		print 'thread %s >>> %s' % (threading.current_thread().name, n)
		time.sleep(1)
	print 'thread %s ended.\n' % threading.current_thread().name

print 'thread %s is running...\n' % threading.current_thread().name
t = threading.Thread(target=loop, )
t.start()
t.join()
print 'thread %s ended.\n' % threading.current_thread().name 
