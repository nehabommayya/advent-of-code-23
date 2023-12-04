def is_gear_symbol(char):
    if char == "*":
        symbol = True
    else:
        symbol = False
    return symbol


def find_asterisks(lines):
    asterisks_in_lines = {}
    line_number = 0

    for line in lines:
        line_number += 1
        chars = list(line.strip())
        asterisks_in_this_line = {}

        for index, char in enumerate(chars):
            if is_gear_symbol(char):
                asterisks_in_this_line[index] = char

        if asterisks_in_this_line:
            asterisks_in_lines[line_number] = asterisks_in_this_line

    return asterisks_in_lines


def find_gear_ratios(asterisks_in_lines, lines):
    gear_ratios_sum = 0

    for line_num, asterisk_dict in asterisks_in_lines.items():
        for position, _ in asterisk_dict.items():
            part_nums = []
            processed_positions = set()

            for i in range(line_num - 2, line_num + 1):
                if 0 <= 1 < len(lines):
                    for j in range(max(0, position - 1), min(position + 2, len(lines[i]))):
                        if lines[i][j].isdigit() and (i, j) not in processed_positions:
                            num, next_pos = extract_full_num(lines, i, j)
                            part_nums.append(num)
                            for k in range (j, next_pos):
                                processed_positions.add((i, k))
                            if len(part_nums) == 2:
                                break

                    if len(part_nums) == 2:
                        break

            if len(part_nums) == 2:
                gear_ratio = part_nums[0] * part_nums[1]
                gear_ratios_sum += gear_ratio

    return gear_ratios_sum


def extract_full_num(lines, line_id, pos):
    num_str = ''
    start_pos = pos

    while pos >= 0 and lines[line_id][pos].isdigit():
        start_pos = pos
        pos -= 1

    while start_pos < len(lines[line_id]) and lines[line_id][start_pos].isdigit():
        num_str += lines[line_id][start_pos]
        start_pos += 1

    return int(num_str), start_pos


with open("part_1_input.txt", "r") as file:
    text = file.readlines()

print(find_gear_ratios(find_asterisks(text), text))

# find_part_numbers(find_symbols(text), text)
