#Exercise 10: What Was That?

# -*- coding: utf-8 -*-

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."
white_cat = "It's a white %s cat." % '\\'

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
print white_cat

print "\\ Backslash"
print "\' Single (\')"
print "\" Double (\")"
print "\a ASCII Bell (BEL)"
print "\b ASCII Backspace (BS)"
print "\f ASCII Formfeed (FF)"
print "\n ASCII Linefeed (LF)"
print "\N"
print "\r"
print "\t"
print "\v"
print "\ooo"
print "\cb"

while True:
	for i in ["/","-","|","\\","|","*"]:
		print "%s\r" % i,