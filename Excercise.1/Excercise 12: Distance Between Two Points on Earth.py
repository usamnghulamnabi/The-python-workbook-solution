"""The surface of the Earth is curved, and the distance between degrees of longitude
varies with latitude. As a result, finding the distance between two points on the surface
of the Earth is more complicated than simply using the Pythagorean theorem.
Let (t 1 , g 1 ) and (t 2 , g 2 ) be the latitude and longitude of two points on the Earth’s
surface. The distance between these points, following the surface of the Earth, in
kilometers is:
distance = 6371.01 × arccos(sin(t 1 ) × sin(t 2 ) + cos(t 1 ) × cos(t 2 ) × cos(g 1 − g 2 ))
The value 6371.01 in the previous equation wasn’t selected at random. It is the
average radius of the Earth in kilometers.
Create a program that allows the user to enter the latitude and longitude of two
points on the Earth in degrees. Your program should display the distance between
the points, following the surface of the earth, in kilometers."""

import math
from math import *

g1_in = float(input("Enter g1 value in degrees: "))
t1_in = float(input("Enter t1 value in degrees: "))
g2_in = float(input("Enter g2 value in degrees: "))
t2_in = float(input("Enter t2 value in degrees: "))

g1_rads = math.radians(g1_in)
g2_rads = math.radians(g2_in)
t1_rads = math.radians(t1_in)
t2_rads = math.radians(t2_in)

distance = 6371.01 * math.acos(sin(t1_rads) * sin(t2_rads) + cos(t1_rads ) * cos(t2_rads) * cos(g1_rads - g2_rads))
print(distance)
