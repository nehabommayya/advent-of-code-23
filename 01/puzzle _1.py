input = open('puzzle_input_1.txt', 'r')
lines = input.readlines()

cal_nums_list = []

for line in lines:
    chars = list(line)
    str = ''
    for char in chars:
        if char.isnumeric():
            str += char
    cal_num = str[0] + str[(len(str) -1)]
    cal_nums_list.append(int(cal_num))

print(cal_nums_list)
print(sum(cal_nums_list))

        #cal_num = str[0] + str[len(str)-1]
    #cal_nums_list.append(int(cal_num))


