headers = [
    "seed-to-soil map:",
    "soil-to-fertilizer map:",
    "fertilizer-to-water map:",
    "water-to-light map:",
    "light-to-temperature map:",
    "temperature-to-humidity map:",
    "humidity-to-location map:"
]


def extract_maps(headers_list):
    maps = {header: [] for header in headers_list}
    current_header = None

    with open("input.txt", "r") as file:
        for line in file:
            line = line.strip()
            if line in headers_list:
                current_header = line
            elif current_header and line:
                maps[current_header].append(line)
            elif not line:
                current_header = None

    return maps


def extract_seed_nums():
    seeds = []
    with open("input.txt", "r") as file:
        for line in file:
            line = line.strip()
            if line.startswith("seeds:"):
                is_seeds = True
                line = line.replace("seeds:", "").strip()
                if line:
                    seeds.extend([int(num) for num in line.split()])

            elif is_seeds:
                if line:
                    seeds.extend([int(num) for num in line.split()])
                else:
                    break
    return seeds


def process_map(source_num_list, map_str):
    dest_nums = []
    req_map = maps_dict[map_str]

    for num in source_num_list:  # for each source num
        source_num = num
        dest_num = source_num

        for line in req_map:
            lino = line.split()

            range_length = int(lino[2])

            source_range_start = int(lino[1])
            source_range_end = source_range_start + range_length

            dest_range_start = int(lino[0])
            dest_range_end = dest_range_start + range_length

            if source_num in range(source_range_start, source_range_end):
                increment = source_num - source_range_start
                dest_num = dest_range_start + increment
                dest_nums.append(dest_num)

        if dest_num == source_num:
            dest_nums.append(dest_num)

    return dest_nums


def process_all_maps(nums, headers):
    current_nums = nums
    for header in headers:
        current_nums = process_map(current_nums, header)
    return current_nums


maps_dict = (extract_maps(headers))
seed_nums = extract_seed_nums()

test = process_all_maps(seed_nums, headers)
print(test)
print(min(test))
