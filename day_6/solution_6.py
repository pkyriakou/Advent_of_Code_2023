def parse_input_multiple_races(input_path):
    with open(input_path) as input_text:
        race_info = input_text.read().split("\n")
        times = [int(time) for time in race_info[0].split(":")[1].split()]
        distances = [int(distance) for distance in race_info[1].split(":")[1].split()]
        races = [(times[i], distances[i]) for i in range(0, len(times))]
    return races

def parse_input_one_race(input_path):
    with open(input_path) as input_text:
        race_info = input_text.read().split("\n")
        time = int(race_info[0].split(":")[1].replace(" ", ""))
        distance = int(race_info[1].split(":")[1].replace(" ", ""))
    return [(time, distance)]

def calculate_distance_travelled(time_pressed, overall_time):
    return (overall_time-time_pressed)*time_pressed

def find_winning_races(input_path, multi_race=True):
    races = parse_input_multiple_races(input_path) if multi_race else parse_input_one_race(input_path)
    overal_mult = 1
    for race in races:
        race_winning_configs = 0
        for trial in range(0, race[0]+1):
            distance_travelled = calculate_distance_travelled(trial, race[0])
            if distance_travelled > race[1]:
                race_winning_configs += 1
        overal_mult *= race_winning_configs
    return overal_mult


print(find_winning_races("day_6/input_6_ex.txt"))
print(find_winning_races("day_6/input_6.txt"))
print(find_winning_races("day_6/input_6_ex.txt", False))
print(find_winning_races("day_6/input_6.txt", False))
