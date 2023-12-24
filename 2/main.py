# Read input from file
file = open('input.txt', 'r')
input = file.read().splitlines()

RED_MAX = 12
GREEN_MAX = 13
BLUE_MAX = 14


def parse_game_id(game_string):
    game_id = game_string.split(' ')[1]
    return int(game_id)


# input = x red, y green, z blue
def parse_cubes(cubes):
    cubes_split = cubes.split(',')

    red = 0
    green = 0
    blue = 0

    for cube_result in cubes_split:
        if (cube_result.count('red') > 0):
            red = cube_result.strip().split(' ')[0]
        if (cube_result.count('green') > 0):
            green = cube_result.strip().split(' ')[0]
        if (cube_result.count('blue') > 0):
            blue = cube_result.strip().split(' ')[0]

    return (int(red), int(green), int(blue))


def is_game_possible(game):
    is_possible = True

    draws = game.split(';')
    for draw in draws:
        game_result = parse_cubes(draw)
        print(game_result)
        if (game_result[0] > RED_MAX or game_result[1] > GREEN_MAX or game_result[2] > BLUE_MAX):
            is_possible = False
            break

    return is_possible


sum_of_possible_games = 0

for line in input:
    game = line.split(':')
    is_possible = is_game_possible(game[1])
    if (is_possible):
        print(game[0], ' impossible')
        game_id = parse_game_id(game[0])
        sum_of_possible_games += game_id
    else:
        print(game[0], ' possible')

print(sum_of_possible_games)
