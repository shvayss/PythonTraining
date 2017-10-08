# Exercise 4: Variables And Names

# -*- coding: utf-8 -*-
# Defined variable for cars amount
cars = 100
# Defined variable for space in one car
space_in_a_car = 4.0
# Defined variable for drivers amount
drivers = 30
# Defined variable for passengers amount
passengers = 90
# Calculate amount of not driven cars
cars_not_driven = cars - drivers
# Defined variable for driven cars
cars_driven = drivers
# Defined variable for carpool capacity
carpool_capacity = cars_driven * space_in_a_car
# Calculate average amount of passengers per car
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
