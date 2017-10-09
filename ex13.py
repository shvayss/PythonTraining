# Exercise 13: Parameters, Unpacking, Variables

# -*- coding: utf-8 -*-

from sys import argv

script, first, second, third = argv

name = input("What's your name? ")
country = input("Where're you from? ")

print("\nThe script is called:", script)
print("\n"+"Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third + "\n")

print("Nice to meet you %s from %s. (%s)" % (name, country, second))
