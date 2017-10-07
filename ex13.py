#Exercise 13: Parameters, Unpacking, Variables

# -*- coding: utf-8 -*-

from sys import argv

script, first, second, third = argv
name = raw_input ("What's your name?")
country = raw_input ("Where're you from?")

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

print "Nice to meet you %s from %s. (%s)" % (name, country, second)