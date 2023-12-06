import re

with open("input.txt", "r") as file:
    text = file.read()


def get_winning_nums(data):
    winning_nums = re.findall(r':\s*(.*?)\s*\|', data)
    winning_dict = {index + 1: list(map(int, item.split())) for index, item in enumerate(winning_nums)}
    return winning_dict


def get_elf_nums(data):
    elf_nums = (re.findall(r'\|\s*(.*)', data))
    elf_dict = {index + 1: list(map(int, item.split())) for index, item in enumerate(elf_nums)}
    return elf_dict


def get_card_matches(winning_dict, elf_dict):
    # creating matches dictionary
    card_matches = {}

    for elf_key, elf_values in elf_dict.items():
        common_nums = [num for num in elf_values if num in winning_dict[elf_key]]
        num_matches_in_card = len(common_nums)
        card_matches[elf_key] = {'num_matches': num_matches_in_card, 'quantity': 1}
    return card_matches


matches_dict = get_card_matches(get_winning_nums(text), get_elf_nums(text))

count = 6

temp_dict = matches_dict.copy()


for key, value in matches_dict.items():
    num_matches = value['num_matches']
    quantity = value["quantity"]
    if num_matches > 0:
        for i in range(1, num_matches + 1):
            temp_dict[key + i]['quantity'] += quantity
            count += 1

matches_dict.update(temp_dict)

total_quantity = sum(card['quantity'] for card in matches_dict.values())

print(total_quantity)

