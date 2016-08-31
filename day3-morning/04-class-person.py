#!/usr/bin/env python

class Person(object):
    def __init__(my_stuff, parents_choice, gender):
        my_stuff.name = parents_choice
        my_stuff.identity = gender
        
    def say_hello(my_stuff):
        print "Hello world, my name is {}".format(my_stuff.name)
        #print "Hello world, my name is %s" % self.name
        #print "Hello world, my name is " + self.name
        
    def change_name(my_stuff, new_name):
        my_stuff.name = new_name
        

jt = Person("James", "male")
pd = Person("Peter", "male")

jt.say_hello()
pd.say_hello()

pd.change_name("Batman")
jt.say_hello()
pd.say_hello()











