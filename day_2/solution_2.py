import math

def is_game_possible(input_path):
    with open(input_path) as text_input:
        game_configs = text_input.read().split("\n")
        ball_limits = {"blue": 14, "red": 12, "green": 13}
        id_sum = 0
        for game in game_configs:
            game_parts = game.split(":")
            game_id = game_parts[0].split()[1]
            sets = game_parts[1].split(";")
            possible = True
            for game_set in sets:
                game_set_balls = {"blue": 0, "red": 0, "green": 0}
                draws = game_set.split(",")
                for draw in draws:
                    info = draw.split()
                    colour = info[1]
                    new_balls_no = game_set_balls[colour] + int(info[0])
                    if new_balls_no > ball_limits[colour]:
                        possible = False
                    else:
                        game_set_balls[colour] = new_balls_no
            if possible:
                id_sum += int(game_id)
    return id_sum

def make_game_possible(input_path):
    with open(input_path) as text_input:
        game_configs = text_input.read().split("\n")
        ball_power_sum = 0
        for game in game_configs:
            game_parts = game.split(":")
            sets = game_parts[1].split(";")
            min_game_balls = {"blue": 0, "red": 0, "green": 0}
            game_power = 0
            for game_set in sets:
                draws = game_set.split(",")
                for draw in draws:
                    info = draw.split()
                    colour = info[1]
                    min_game_balls[colour] = max(int(info[0]), min_game_balls[colour])
            game_power = math.prod(min_game_balls.values())
            ball_power_sum += game_power
    return ball_power_sum


print(make_game_possible("day_2/input_2.txt"))
