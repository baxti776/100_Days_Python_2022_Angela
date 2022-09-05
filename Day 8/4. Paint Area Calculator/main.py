import math


def paint_area():
    height_input = int(input("Enter height: "))
    width_input = int(input("Enter width: "))
    cover = 5
    print(f"You need {math.ceil((height_input * width_input) / cover)} cans of color")


paint_area()
