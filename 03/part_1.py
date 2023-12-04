def is_symbol(char):
    if char.isdigit() or char == ".":
        symbol = False
    else:
        symbol = True
    return symbol


def find_symbols(lines):
    symbols_in_lines = {}
    line_number = 0

    for line in lines:
        line_number += 1
        chars = list(line.strip())
        symbols_in_this_line = {}

        for index, char in enumerate(chars):
            if is_symbol(char):
                symbols_in_this_line[index] = char

        if symbols_in_this_line:
            symbols_in_lines[line_number] = symbols_in_this_line

    return symbols_in_lines


def find_part_numbers(symbols_in_lines, lines):
    total_sum = 0
    processed_nums = {}

    # print(symbols_in_lines.items())
    for line_num, symbol_dict in symbols_in_lines.items():  # items are the line numbers where there is a symbol
        for position, symbol in symbol_dict.items():

            for i in range(line_num - 2, line_num + 1):

                if 0 <= 1 < len(lines):

                    for j in range(max(0, position - 1), min(position + 2, len(lines[i]))):

                        if lines[i][j].isdigit():
                            num, next_pos = extract_full_num(lines, i, j)

                            if (i, next_pos - 1) not in processed_nums.get((line_num - 1, position), set()):
                                total_sum += num
                                processed_nums.setdefault((line_num - 1, position), set()).add((i, next_pos - 1))
                                j = next_pos - 1

    return total_sum


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

print(find_part_numbers(find_symbols(text), text))

# find_part_numbers(find_symbols(text), text)
