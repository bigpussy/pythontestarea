# -*- coding: utf-8 -*-
print u"wsgi"

def application(environ, start_response):
	start_response('200 OK',[('Content-Type','text/html')])
	method = environ['REQUEST_METHOD']
	print method
	return '<h1>Hello,%s!</h1>' % (environ['PATH_INFO'][1:] or 'web')


