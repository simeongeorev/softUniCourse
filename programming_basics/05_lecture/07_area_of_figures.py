# input string
import math

figure = str(input())

if figure == "square":
    square_side = float(input())
    print(square_side ** 2)

elif figure == "rectangle":
    rect_side_a = float(input())
    rect_side_b = float(input())
    print(rect_side_a * rect_side_b)

elif figure == "circle":
    circle_radius = float(input())
    print(math.pi * circle_radius ** 2)

elif figure == "triangle":
    triangle_base = float(input())
    triangle_height = float(input())
    print(triangle_base * triangle_height / 2)
