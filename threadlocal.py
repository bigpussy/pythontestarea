# -*- coding: utf-8 -*-

import threading

class Student(object):
	pass
	
#local_school = threading.local()
local_school = Student()

def process_student():
	print 'Hello, %s (in %s)' % (local_school.student, threading.current_thread().name)
	
def process_thread(name):
	global local_school
	local_school.student = name
	process_student()

for i in range(10):
	t = threading.Thread(target=process_thread, args=('student%d' % i,), name='Thread-%d' % i)
	t.start()
	





