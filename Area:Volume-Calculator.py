'''
Write a program that takes as input a single length (a float) and calculates the following:

• The area of a square with side of that length
• The volume of a cube with side of that length
• The area of a circle with radius of that length
• The volume of a sphere with radius of that length
• The volume of a cylinder with radius of that length and side of that length

Import the math module and use the constant math.pi for the value π.

When the length is entered by the user, the program should check that it is non-negative.

If the length is negative, the message “Length must be >= 0. Please try again.”
should be printed out and the program should exit.
'''


length = float(input('Enter the length: '))
width = length
height = length
radius = length

import math

if length >= 0:
    area = length * width
    print('Area of square is: ', area)
    volume = length * width * height
    print('Volume of cube is:', volume)
    print('Area of circle is:', math.pi * radius ** 2)
    print('Volume of sphere is:', 4/3 * math.pi * radius ** 3)
    area_of_base = math.pi * radius ** 2 
    print('Volume of cylinder is:', area_of_base * length)
else:
    print('Length must be >= 0. Please try again.')
    print('Finished!')
    

