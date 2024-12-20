""" Monkey Patching in a Third-Party Library """

import math

def area_of_circle(radis):
    return math.pi * radis ** 2

math.area_of_circle = area_of_circle

print(math.area_of_circle(2))
