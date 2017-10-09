# Exercise 11: Asking Questions

# -*- coding: utf-8 -*-
print("How old are you?", end=" ")
age = input('--> ')
print("How tall are you (cm)?", end=" ")
height = input('--> ')
print("How much do you weight (kg)?", end=" ")
weight = input('--> ')

print("So, you're %r years old, %s cm tall and %s kg heavy." % (
    age, height, weight))
