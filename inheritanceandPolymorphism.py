# -*- coding: utf-8 -*-
print u"继承和多态"

class Animal(object):
	def run(self):
		print 'Animal is running...'
	def __len__(self):
		return 100
class Dog(Animal):
	def run(self):
		print 'Dog is running...'
class Cat(Animal):
	def run(self):
		print 'Cat is running...'

dog = Dog()
cat = Cat()

dog.run()
cat.run()

a = list()

b = Animal()

c = Dog()

print isinstance(a, list)
print isinstance(b, Animal)
print isinstance(c, Dog)
print isinstance(c, Animal)
class Tortoise(object):
	def run(self):
		print "Tortoise is running"

def run_twice(animal):
	animal.run()
	animal.run()
run_twice(Tortoise())

print type(a)
print type(b)
import types

print types
print "end"
