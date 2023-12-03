import re

input = open('puzzle_input_2.txt', 'r')
lines = input.readlines()


def word_to_number(str):
    map = {
        'one': '1', 'two': '2', 'three': '3',
        'four': '4', 'five': '5', 'six': '6',
        'seven': '7', 'eight': '8', 'nine': '9'
    }
    return map.get(str, str)


cal_nums = []

for line in lines:
    # chars = list(line)
    found_nums = re.findall(r'one|two|three|four|five|six|seven|eight|nine|\d', line)
    formatted_nums = [word_to_number(num) for num in found_nums]

    cal_num = int(formatted_nums[0] + formatted_nums[len(formatted_nums) - 1])
    cal_nums.append(cal_num)

print(cal_nums)
print(sum(cal_nums))

input.close()