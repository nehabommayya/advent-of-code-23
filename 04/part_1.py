import re

with open("input.txt", "r") as file:
    text = file.read()


def get_winning_nums(data):
    winning_nums = re.findall(r':\s*(.*?)\s*\|', data)
    winning_nums = [list(map(int, item.split())) for item in winning_nums]
    print(winning_nums)
    return winning_nums


def get_elf_nums(data):
    elf_nums = (re.findall(r'\|\s*(.*)', data))
    elf_nums = [list(map(int, item.split())) for item in elf_nums]
    print(elf_nums)
    return elf_nums


def compare_nums(winning_nums, elf_nums):
    points = []
    for i in range(0, len(winning_nums)):
        matches = []
        for item in elf_nums[i]:
            if item in winning_nums[i]:
                matches.append(item)
        card_points = 0
        if len(matches) > 0:
            card_points = 1
            for j in range(0, len(matches)-1):
                card_points *= 2
        points.append(card_points)

    return sum(points)


print(compare_nums(get_winning_nums(text), get_elf_nums(text)))
