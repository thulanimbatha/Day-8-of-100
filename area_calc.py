# using functions
# calculate number of cans needed to paint a wall

def num_cans(width, height, coverage):
    area = width * height
    can_num = area / coverage
    print(can_num, f"\nSo number of cans needed is: {round(can_num)}")

w = int(input("Enter the width of the wall: "))
h = int(input("Enter the height of the wall: "))
c = 5

num_cans(width = w, height = h, coverage = c)