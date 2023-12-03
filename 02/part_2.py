import re

with open('part_1_input.txt', 'r') as file:
    lines = file.readlines()

powers = []

for line in lines:
    game_id = int(line.split()[1][:-1])

    red_nums = re.findall(r'(\d+)\s*red', line)
    max_red = int(red_nums[0])
    for num in red_nums:
        if int(num) > max_red:
            max_red = int(num)


    green_nums = re.findall(r'(\d+)\s*green', line)
    max_green = int(green_nums[0])
    for num in green_nums:
        if int(num) > max_green:
            max_green = int(num)

    blue_nums = re.findall(r'(\d+)\s*blue', line)
    max_blue = int(blue_nums[0])
    for num in blue_nums:
        if int(num) > max_blue:
            max_blue = int(num)

    cubes_power = max_red * max_green * max_blue
    powers.append(cubes_power)

print(sum(powers))
