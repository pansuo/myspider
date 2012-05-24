#!/usr/bin/env python
#coding=utf-8

import urllib2
import urllib
import os
import sys

class Person:
	population = 0
	def __init__(self,name):
		self.name = name
		self.age= 10
		Person.population += 1
		print 'new guy %s created,now totally %d person' % (self.name,Person.population)

	def __del__(self):
		Person.population -= 1
		print 'a guy %s died' % self.name

	def sayHi(self):
		print "hello,how are you,I'm",self.name,"and my age is",self.age
	
class Teacher(Person):
	members = 0
	def __init__(self,name,majority):
		Person.__init__(self,name)
		self.major=majority
		Teacher.members += 1
		print 'new teacher %s coming,now totally %d teachers' %(self.name,Teacher.members)

	def __del__(self):
		Person.__del__(self)
		Teacher.members -= 1
		print 'a teacher %s from %s school died' % (self.name,self.major)
		

	def sayHi(self):
		print "Yo,I am a teacher of"+self.major+" school"
		


p1=Person("monk liu")
p1.sayHi()
print p1.name+"'s age is "+str(p1.age)

p2=Teacher("Bow","Art")
p2.sayHi()





