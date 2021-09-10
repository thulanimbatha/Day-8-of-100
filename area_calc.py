# using functions
# calculate number of cans needed to paint a wall

def paint_calc(width, height, coverage):
    area = width * height
    num_cans = area / coverage
    print(num_cans, f"\nSo number of cans needed is: {round(num_cans)}")

w = int(input("Enter the width of the wall: "))
h = int(input("Enter the height of the wall: "))
c = 5

paint_calc(width = w, height = h, coverage = c)