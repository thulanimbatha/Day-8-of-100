# using functions
# calculate number of cans needed to paint a wall
import math

def paint_calc(width, height, coverage):
    area = width * height
    num_cans = area / coverage
    print(num_cans, f"\nSo number of cans needed is: {math.ceil(num_cans)}")    # round() function doesn't work - we need to round UP (5.4 = 6 not 5.4 = 5)

w = int(input("Enter the width of the wall: "))
h = int(input("Enter the height of the wall: "))
c = 5

paint_calc(width = w, height = h, coverage = c)