# -*- coding: utf-8 -*-
print u"条件判断"

import unittest

from mydict import Dict

class Testdict(unittest.TestCase):
	def test_init(self):
		d = Dict(a = 1, b = 'test')
		self.assertEquals(d.a, 1)
		self.assertEquals(d.b, 'test')
		self.assertTrue(isinstance(d, dict))
	
	def test_key(self):
		d = Dict()
		d['key'] = 'value'
		self.assertEquals(d.key, 'value')
	
	def test_attr(self):
		d = Dict()
		d.key = 'value'
		self.assertTrue('key' in d)
		self.assertEquals(d['key'], value)
	
	
	def test_keyerror(self):
		d = Dict()
		with self.assertRaises(keyError):
			value = d['empty']
	
	def test_attrerror(self):
		print 'test_arrterror'
		with self.assertRaise(AttributeError):
			value = d.empty


