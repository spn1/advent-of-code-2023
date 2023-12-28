# Read input from file
file = open('input.txt', 'r')
input = file.read().splitlines()

# Get symbols
# symbols = []
# for line in input:
#     for char in line:
#         if (char.isdigit() or char == '.' or char in symbols):
#             continue
#         symbols.append(char)

# Constants
symbols = ['-', '*', '&', '$', '@', '/', '#', '=', '%', '+']
line_length = len(input[0])
part_numbers = []


def check_horizontally_adjacent_cells(line, index):
    if line == None:
        return False

    adjacent_to_symbol = False

    if (index > 0):
        adjacent_to_symbol = line[index - 1] in symbols
    if (index < line_length - 1 and not(adjacent_to_symbol)):
        adjacent_to_symbol = line[index + 1] in symbols

    return adjacent_to_symbol


def check_vertically_adjacent_cells(line, index):
    if line == None:
        return False

    return line[index] in symbols


def has_vertically_or_diagonally_adjacent_symbol(previous_line, next_line, index):
    """
    Check if the vertically or diagonally adjacent lines have symbols next to the given index

    :param previous_line: The line above the current line (None if top line)
    :param next_line: The line below the current line (None if bottom line)
    :return: True or False if there is a vertically or diagonally adjacent symbol
    """
    adjacent_to_symbol = False

    adjacent_to_symbol = \
        check_horizontally_adjacent_cells(previous_line, index) or \
        check_horizontally_adjacent_cells(next_line, index) or \
        check_vertically_adjacent_cells(previous_line, index) or \
        check_vertically_adjacent_cells(next_line, index)

    return adjacent_to_symbol


def has_horizontally_adjacent_symbol(line, index):
    """
    Check if the horizontally adjacent characters to the given index are symbols

    :param line: The line with the character
    :return: True or False if there is a horizontally adjacent symbol
    """
    return check_horizontally_adjacent_cells(line, index)


def has_adjacent_symbol(previous_line, current_line, next_line, index):
    """
    Checks the adjacent positions of the specified index in the current line for a symbol

    :param previous_line: The line before the current_line
    :param current_line: The line where the digit is
    :param next_line: The line after the current_line
    :return: True or False depending on if there is a symbol adjacent to the given index in the current_line
    """
    has_adjacent_symbol =  \
        has_horizontally_adjacent_symbol(current_line, index) or \
        has_vertically_or_diagonally_adjacent_symbol(
            previous_line, next_line, index)

    return has_adjacent_symbol


def get_part_number(line, index):
    """
    For the given line, fetches the full part number at the particular index

    :param line: The line the number is on
    :param index: The index of the digit that has an adjacent symbol
    :return: The full part number
    """
    # Record digits backwards and forwards from index, until you get to a symbol or .
    part_number = []
    initial_digit = line[index]

    #  - Get previous digits
    previous_digits = []
    previous_index = index - 1
    while previous_index >= 0 and line[previous_index].isdigit():
        previous_digits.insert(0, line[previous_index])
        previous_index -= 1

    #  - Get next digits
    next_digits = []
    next_index = index + 1
    while next_index < line_length and line[next_index].isdigit():
        next_digits.append(line[next_index])
        next_index += 1

    # Merge digits into single string and convert to integer
    part_number.extend(previous_digits)
    part_number.append(initial_digit)
    part_number.extend(next_digits)
    return part_number, len(next_digits)


for row_index, line in enumerate(input):
    column_index = 0
    while column_index < line_length:
        char = line[column_index]
        if (char.isdigit()):
            previous_line = input[row_index - 1] \
                if row_index > 0 \
                else None
            next_line = input[row_index + 1] \
                if row_index < len(input) - 1 \
                else None

            if (has_adjacent_symbol(previous_line, line, next_line, column_index)):
                # Get full integer
                part_number, skip = get_part_number(line, column_index)
                part_numbers.append(int(''.join(part_number)))
                column_index += skip

        column_index += 1


print(part_numbers)
print(sum(part_numbers))
