# Exercise 14: Prompting and Passing

# -*- coding: utf-8 -*-

from sys import argv

script, user_name, user_second_name = argv
prompt = "*****$ "

print("Hi %s %s, I'm the %s script." % (user_name, user_second_name, script))
print("I'd like to ask you a few questions.")
print("Do you like me %s %s?" % (user_name, user_second_name))
likes = input(prompt)

print("Where do you live %s %s?" % (user_name, user_second_name))
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print("""
Alright, so you, %s %s, said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.""" % (user_name, user_second_name, likes, lives, computer))
