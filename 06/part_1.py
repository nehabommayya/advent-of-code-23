from functools import reduce


def get_records():
    with open("input.txt", "r") as file:
        data = {}
        lines = file.readlines()

        times = [int(time) for time in lines[0].split()[1:]]  #
        distances = [int(distance) for distance in lines[1].split()[1:]]

        for index in range(len(times)):
            data[index] = (times[index], distances[index])

        print(data)
        return data


def calc_time_combos(records):
    total_combos = []
    for key in records:
        num_combos = 0
        time = records[key][0]
        record_distance = records[key][1]
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

answer = reduce(lambda x, y: x * y, combos_list)

print(answer)