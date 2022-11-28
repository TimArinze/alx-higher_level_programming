#!/usr/bin/python3
Circle = __import__('103-magic_class').MagicClass

my_circle_1 = Circle(3)
print("Area: {}".format(my_circle_1.area()))

try:
    print(my_circle_1.radius)
except Exception as e:
    print(e)

try:
    print(my_circle_1.__radius)
except Exception as e:
    print(e)

my_circle_2 = Circle(5)
print("Circumference: {}".format(my_circle_2.circumference()))
