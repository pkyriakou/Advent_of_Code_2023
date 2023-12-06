def parse_input(input_path):
    schematic = []
    with open(input_path) as input_text:
        schematic = [list(row) for row in input_text.read().split("\n")]
    return schematic

def find_number_coords(engine_schema):
    number_coords = []
    for row in range(0, len(engine_schema)):
        start_coord = -1
        end_coord = -1
        for column in range(0, len(engine_schema)):
            if engine_schema[row][column].isdigit():
                if start_coord == -1:
                    start_coord = column
                elif column == len(engine_schema) - 1:
                    end_coord = column
                    number_coords.append((row, start_coord, end_coord))
                    start_coord = end_coord = -1
            else:
                if start_coord != -1:
                    end_coord = column - 1
                    number_coords.append((row, start_coord, end_coord))
                    start_coord = end_coord = -1
    return number_coords

def find_area_around_number(number_coords, size):
    neighbours = []
    if number_coords[0] < size - 1:  # not bottom row:
        neighbours += [(number_coords[0]+1, i) for i in range(number_coords[1], number_coords[2]+1)]  # coordinates under
    if number_coords[2] < size - 1:  # not right
        neighbours += [(number_coords[0], number_coords[2]+1)]  # coordinate to the right
    if number_coords[0] < size - 1 and number_coords[2] < size - 1:  # not bottom right
        neighbours += [(number_coords[0]+1, number_coords[2]+1)]  # coordinate under n right
    if number_coords[0] < size - 1 and number_coords[1] != 0:
        neighbours += [(number_coords[0]+1, number_coords[1]-1)]  # coordinate under n left
    if number_coords[0] != 0:  # not top row
        neighbours += [(number_coords[0]-1, i) for i in range(number_coords[1], number_coords[2]+1)]  # coordinates over
    if number_coords[1] != 0:  # not left
        neighbours += [(number_coords[0], number_coords[1]-1)]  # coordinate to the left
    if number_coords[0] != 0 and number_coords[2] < size - 1:  # not top right
        neighbours += [(number_coords[0]-1, number_coords[2]+1)]  # coordinate over n right
    if number_coords[0] != 0 and number_coords[1] != 0:  # not top left
        neighbours += [(number_coords[0]-1, number_coords[1]-1)]  # coordinate over n left
    return neighbours

def is_part_number(neighbour_coords, engine_schema):
    for neighbor in neighbour_coords:
        if engine_schema[neighbor[0]][neighbor[1]] != "." and not engine_schema[neighbor[0]][neighbor[1]].isdigit():
            return True
    return False

def get_number_from_coords(number_coords, engine_schema):
    return "".join([engine_schema[number_coords[0]][index] for index in range(number_coords[1], number_coords[2]+1)])

def find_gear_coords(engine_schema):
    gear_coords = []
    for row in range(0, len(engine_schema)):
        for column in range(0, len(engine_schema)):
            if engine_schema[row][column] == "*":
                gear_coords.append((row, column))
    return gear_coords

def get_gear_neighbours(gear_coords, size):
    neighbours = []
    if gear_coords[0] < size - 1:  # not bottom row:
        neighbours += [(gear_coords[0]+1, gear_coords[1])]  # coordinates under
    if gear_coords[1] < size - 1:  # not right
        neighbours += [(gear_coords[0], gear_coords[1]+1)]  # coordinate to the right
    if gear_coords[0] < size - 1 and gear_coords[1] < size - 1:  # not bottom right
        neighbours += [(gear_coords[0]+1, gear_coords[1]+1)]  # coordinate under n right
    if gear_coords[0] < size - 1 and gear_coords[1] != 0:
        neighbours += [(gear_coords[0]+1, gear_coords[1]-1)]  # coordinate under n left
    if gear_coords[0] != 0:  # not top row
        neighbours += [(gear_coords[0]-1, gear_coords[1])]  # coordinates over
    if gear_coords[1] != 0:  # not left
        neighbours += [(gear_coords[0], gear_coords[1]-1)]  # coordinate to the left
    if gear_coords[0] != 0 and gear_coords[1] < size - 1:  # not top right
        neighbours += [(gear_coords[0]-1, gear_coords[1]+1)]  # coordinate over n right
    if gear_coords[0] != 0 and gear_coords[1] != 0:  # not top left
        neighbours += [(gear_coords[0]-1, gear_coords[1]-1)]  # coordinate over n left
    return neighbours

def find_gear_numbers(gear_neighbours, number_coords):
    gear_nums = []
    for neighbour in gear_neighbours:
        for index, number in enumerate(number_coords):
            if neighbour[0] == number[0] and neighbour[1] in range(number[1], number[2]+1):
                gear_nums.append(number)
                number_coords.pop(index)
    return gear_nums

def find_engine_parts(input_path):
    part_number_sum = 0
    engine_schema = parse_input(input_path)
    numbers = find_number_coords(engine_schema)
    for number in numbers:
        neighbours = find_area_around_number(number, len(engine_schema))
        if is_part_number(neighbours, engine_schema):
            part_number_sum += int(get_number_from_coords(number, engine_schema))
    return part_number_sum

def find_gear_ratios(input_path):
    gear_ratio_sum = 0
    engine_schema = parse_input(input_path)
    gears = find_gear_coords(engine_schema)
    numbers = find_number_coords(engine_schema)
    for gear in gears:
        gear_neighbours = get_gear_neighbours(gear, len(engine_schema))
        gear_numbers = find_gear_numbers(gear_neighbours, numbers)
        if len(gear_numbers) == 2:
            gear_ratio = int(get_number_from_coords(gear_numbers[0], engine_schema)) * int(get_number_from_coords(gear_numbers[1], engine_schema))
            gear_ratio_sum += gear_ratio
    return gear_ratio_sum


print(find_engine_parts("day_3/input_3_ex.txt"))
print(find_engine_parts("day_3/input_3.txt"))
print(find_gear_ratios("day_3/input_3_ex.txt"))
print(find_gear_ratios("day_3/input_3.txt"))
