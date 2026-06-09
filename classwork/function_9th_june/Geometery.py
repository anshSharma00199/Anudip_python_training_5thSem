'create a python programming which provides the menu to the user to select the 2D figures(Circle,Triangle, Square).'
'After selcting figure User is again asked to provide the input of corresponding data for the figure. '
'After input of corresponding data again provide a menu to select the operation-> area, perimeter and as per the data provided by the user display the result of operation.'
'This task will be repeated again and untill user selects the option 2. exit fronm that figure.'
import math

# Circle
def area_circle(r):
    return math.pi * r * r

def perimeter_circle(r):
    return 2 * math.pi * r

# Square
def area_square(side):
    return side * side

def perimeter_square(side):
    return 4 * side

# Triangle
def area_triangle(base, height):
    return 0.5 * base * height

def perimeter_triangle(a, b, c):
    return a + b + c

#rectangle
def rectangle(length,breadth):
    return length*breadth
def perimeter_rectangle(length,breadth):
    return 2*(length+breadth)