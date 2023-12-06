def sensor_reading_calibrator(input_path, advanced_calibration):
    overall_sum = 0
    with open(input_path) as text_input:
        lines = text_input.read().split("\n")
        for line in lines:
            if not len(line):
                continue
            first_number = find_first_num(line, advanced_calibration)
            second_number = find_second_num(line, advanced_calibration)
            overall_sum += int(first_number + second_number)
    print(overall_sum)

def find_first_num(line, advanced_calibration):
    first_num_pointer = 1
    while first_num_pointer <= len(line):
        result = is_there_valid_number(line[:first_num_pointer], -1, advanced_calibration)
        if result:
            return result
        first_num_pointer += 1

def find_second_num(line, advanced_calibration):
    last_num_pointer = len(line) - 1
    while last_num_pointer >= 0:
        result = is_there_valid_number(line[last_num_pointer:], 0, advanced_calibration)
        if result:
            return result
        last_num_pointer -= 1


def is_there_valid_number(current_reading, new_elem_index, advanced_calibration):
    num_strs = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    if advanced_calibration and len(current_reading) >= 3:
        for num, value in num_strs.items():
            if num in current_reading:
                return value
    if current_reading[new_elem_index].isdigit():
        return current_reading[new_elem_index]


sensor_reading_calibrator("input_1.txt", False)
