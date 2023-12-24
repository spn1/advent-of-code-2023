import math

# Read input from file
file = open('input.txt', 'r')
input = file.read().splitlines()

# Max cube counts for part 1
RED_MAX = 12
GREEN_MAX = 13
BLUE_MAX = 14


def parse_game_id(game_string):
    """
    Parses the ID of the game from the game string

    :param game_string: The title of the game, before the ':' character
    :return: The game number (int)
    """
    game_id = game_string.split(' ')[1]
    return int(game_id)


# input = x red, y green, z blue
def parse_cubes(cubes):
    """
    For a list of cubes draw from the bag, returns the amount of red, green, and blue cubes drawn

    :param cubes: A string specifying the cubes drawn for a particular draw
    :return: The number of red, green, and blue cubes drawn
    """
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
    """
    Determines if the game is possible by the list of cubes drawn and the max number of each
    cube colour in the bad

    :param game_string: The full list of cubes drawn each time they are drawn in the game
    :return: True or false if the game is possible
    """
    is_possible = True

    draws = game.split(';')
    for draw in draws:
        game_result = parse_cubes(draw)
        if (game_result[0] > RED_MAX or game_result[1] > GREEN_MAX or game_result[2] > BLUE_MAX):
            is_possible = False
            break

    return is_possible


def max_of_cubes_in_game(game):
    """
    Determines the minimum number of cubes required for all the draws in a game to be possible

    :param game_string: The full list of cubes drawn each time they are drawn in the game
    :return: The minimum number of cubes required for a game to be possible
    """
    draws = game.split(';')
    results = [parse_cubes(draw) for draw in draws]
    red_min_cubes = max(r for r, g, b in results)
    green_min_cubes = max(g for r, g, b in results)
    blue_min_cubes = max(b for r, g, b in results)
    return (red_min_cubes, green_min_cubes, blue_min_cubes)


sum_of_possible_games = 0
sum_of_min_cube_powers = 0

for line in input:
    game = line.split(':')

    # Determine if game is possible
    is_possible = is_game_possible(game[1])
    if (is_possible):
        game_id = parse_game_id(game[0])
        sum_of_possible_games += game_id

    # Determine minimum number of cubes for game to be possible
    min_cubes_required = max_of_cubes_in_game(game[1])
    sum_of_min_cube_powers += math.prod([n for n in min_cubes_required])

print(sum_of_possible_games)
print(sum_of_min_cube_powers)
