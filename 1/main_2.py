# Read input from file
file = open('input.txt', 'r')
input = file.read().splitlines()

# Set up digit string values
digits = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    # 'ten',
    # 'eleven',
    # 'twelve',
    # 'thirteen',
    # 'fourteen',
    # 'fifteen',
    # 'sixteen',
    # 'seventeen',
    # 'eigteen',
    # 'nineteen',
    # 'twenty'
    # 'thirty',
    # 'fourty',
    # 'fifty',
    # 'sixty',
    # 'seventy',
    # 'eighty',
    # 'ninety'
}


# Initialize results value
result = {}


def get_first_digit(line):
    # Get index of first integer
    first_digit_index = None
    for char in line:
        if char.isdigit():
            first_digit_index = line.find(char)
            break

    # Get index of first substring
    first_digit_substring_value = None
    first_digit_substring_index = -1
    for digit in digits.keys():
        index = line.find(digit)
        if (index >= 0):
            if (not(first_digit_substring_index == -1) and index > first_digit_substring_index):
                continue
            first_digit_substring_value = digits[digit]
            first_digit_substring_index = index

    # Return the value of whatever comes first in the string
    if (first_digit_substring_index < 0):
        return line[first_digit_index]
    if (first_digit_index < first_digit_substring_index):
        return line[first_digit_index]

    return first_digit_substring_value


def get_last_digit(line):
    last_digit_index = None
    for i in range(len(line)):
        if line[i].isdigit():
            last_digit_index = i

    # Get index of last substring
    last_digit_substring_value = None
    last_digit_substring_index = -1
    for digit in digits.keys():
        index = line.rfind(digit)
        if (index > 0 and index > last_digit_substring_index):
            last_digit_substring_value = digits[digit]
            last_digit_substring_index = index
        # index = line.find(digit)
        # print(index)
        # if (index > 0 and index > last_digit_substring_index):
        #     print('yes')
        #     last_digit_substring_value = digits[digit]
        #     last_digit_substring_index = index

    if (last_digit_substring_index < 0):
        return line[last_digit_index]
    if (last_digit_index > last_digit_substring_index):
        return line[last_digit_index]
    else:
        return last_digit_substring_value


# def get_first_digit(line):
#     for char in line:
#         if char.isdigit():
#             return char


# def get_last_digit(line):
#     val = None
#     for char in line:
#         if char.isdigit():
#             val = char
#     return val


# def format_line(line):
#     numeric_line = line
#     for digit in digits.keys():
#         print(numeric_line)
#         numeric_line = numeric_line.replace(digit, digits[digit])

#     return numeric_line


# Get digits from each line
for line in input:
    print(line)
    # numeric_line = format_line(line)
    # Get first and last digit
    first_digit = get_first_digit(line)
    last_digit = get_last_digit(line)

    # Combine them together
    combined_digit = first_digit + last_digit

    # Add them to sum
    result[line] = int(combined_digit)

for x, y in result.items():
    print(x, ' - ', y)

# Calculate the sum of all combined digits
result_sum = sum(result.values())
print(result_sum)
