# Exercise 5: More Variables And Printing

# -*- coding: utf-8 -*-
name = 'Zed A. Shaw'
age = 35  # not a lie
height = 74  # inches
weight = 180  # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
test = 505
inchcm = 2.54
lbkg = 0.453592
t1 = 3.2
t2 = 15.7

print("Let's talk about %s." % name)
print("He's %d inches tall." % height)
print("He's %f cm tall." % (height * inchcm))
print("He's %d pounds heavy." % weight)
print("He's %f kgs heavy." % (weight * lbkg))
print("Actually that's not too heavy.")
print("He's got %s eyes and %s hair." % (eyes, hair))
print("His teeth are %s depending on the coffee." % teeth)
print("Test task %r." % test)
print("%g inch = %g cm" % (t1, inchcm * t1))
print("%g lbs = %g kgs" % (t2, lbkg * t2))

# this line is tricky, try to get it exactly right
print("If I add %d, %d and %d I get %d." % (
	age, height, weight, age + height + weight))
