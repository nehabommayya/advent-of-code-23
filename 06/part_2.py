from functools import reduce


def get_records():
    with open("input.txt", "r") as file:
        data = []
        lines = file.readlines()

        time = [int(time) for time in lines[0].split()[1:]]  #
        distance = [int(distance) for distance in lines[1].split()[1:]]

        data.append(time)
        data.append(distance)

        print(data)
        return data


def calc_time_combos(records):
    total_combos = []
    num_combos = 0
    time = records[0][0]
    record_distance = records[1][0]
    for i in range(0, time):
        winning_distances = []
        time_held = i  # also the speed
        time_to_move = time - i
        distance = time_held * time_to_move
        if distance > record_distance:
            winning_distances.append(distance)

            num_combos += len(winning_distances)

    total_combos.append(num_combos)

    return total_combos


combos_list = calc_time_combos(get_records())

print(combos_list)