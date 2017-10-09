# Exercise 15: Reading Files

# -*- coding: utf-8 -*-
# include python's 'sys' module
from sys import argv

# define variables where argv data will be stored
script, filename = argv

# assign file object to variable
txt = open(filename)
# print file's name
print("Here's your file %r:" % filename)
# print file's content
print(txt.read())
txt.close()

# ask user for another file name
print("Type the filename again:")
file_again = input("> ")
# assign file object to variable
txt_again = open(file_again)
# print(file's content
print(txt_again.read())
txt_again.close()
