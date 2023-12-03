import re

#12 red, 13 green, 14 blue

with open('part_1_input.txt', 'r') as file:
    lines = file.readlines()

plausible_games = []

for line in lines:
    is_possible = True
    game_id = int(line.split()[1][:-1])

    red_nums = re.findall(r'(\d+)\s*red', line)
    for num in red_nums:
        if int(num) > 12:
            is_possible = False

    green_nums = re.findall(r'(\d+)\s*green', line)
    for num in green_nums:
        if int(num) > 13:
            is_possible = False

    blue_nums = re.findall(r'(\d+)\s*blue', line)
    for num in blue_nums:
        if int(num) > 14:
            is_possible = False

    if is_possible:
        plausible_games.append(game_id)

print(sum(plausible_games))






