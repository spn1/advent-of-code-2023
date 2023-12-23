# Read input from file
file = open('input.txt', 'r')
input = file.read().splitlines()

# Initialize results value
result = {}


def get_first_digit(line):
    for char in line:
        if char.isdigit():
            return char


def get_last_digit(line):
    val = None
    for char in line:
        if char.isdigit():
            val = char
    return val


# Get digits from each line
for line in input:
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
