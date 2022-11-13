#Write a Python program to print the square and cube symbol
#in the area of a rectangle and volume of a cylinder.
#Sample output:
#The area of the rectangle is 1256.66cm2
#The volume of the cylinder is 1254.725cm3
from math import pi

def rectangle_area(length, width):
    return length*width

def cylinder_volume(r, height):
    return pi*r*r*height
print('The area of the rectangle is %.2f cm\u00B2' % rectangle_area(7, 8))
print('The volume of the cylinder is %.2f cm\u00B3' % cylinder_volume(8, 2))