# -*- coding: utf-8 -*-
from sys import argv

script, filename = argv
test = open(filename)

print test.read()

test.close()