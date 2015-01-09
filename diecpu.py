# -*- coding: utf-8 -*-
print u"条件判断"
import threading, multiprocessing

def loop():
	x = 0
	while True:
		x = x ^ 1
print range(4)
for i in range(4):
	t = threading.Thread(target=loop)
	t.start()
