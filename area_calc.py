# using functions
# calculate number of cans needed to paint a wall

def num_cans(width, height, coverage):
    area = width * height
    can_num = area / coverage
    print(can_num, "\n",f"So number of cans needed is: {round(can_num)}")
num_cans(2, 4, 5)