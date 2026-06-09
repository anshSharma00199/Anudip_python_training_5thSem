import math

# Rectangle
#function to print the area of rectangle
def area_rectangle(length, breadth):
    return length * breadth

#function to print the perimeter of rectangle
def perimeter_rectangle(length, breadth):
    return 2 * (length + breadth)
#-------------------------------------------------------

# Square
#function to print the area of square
def area_square(side):
    return side * side
#function to print the perimeter of square
def perimeter_square(side):
    return 4 * side
#-------------------------------------------------------

# Circle
#function to print the Area of circle
def area_circle(radius):
    return math.pi * radius * radius
#function to print the perimter of circle
def perimeter_circle(radius):
    return 2 * math.pi * radius
#-------------------------------------------------------

# Triangle
#function to print the area of triangle
def area_triangle(base, height):
    return 0.5 * base * height
#function to print the perimeter of triangle
def perimeter_triangle(a, b, c):
    return a + b + c