# Exercise 6: Strings And Text

# -*- coding: utf-8 -*-
# Insert 10 to string variable
x = "There are %d types of people." % 10
# define string variables
binary = "binary"
# define string variable
do_not = "don't"
# Insert two string variables to this string variable
y = "Those who know %s and those who %s." % (binary, do_not)

print(x)
print(y)

# use formater for debugging
print("I said: %r." % x)
# use string formater
print("I also said: '%s'." % y)

# define boolean variable
hilarious = False
# Insert boolean variable to string varible
joke_evaluation = "Isn't that joke so funny?! %r"

print(joke_evaluation % hilarious)

w = "This is the left side of..."
e = "a string with right side"

# Concatanate string variables
print(w + e)
