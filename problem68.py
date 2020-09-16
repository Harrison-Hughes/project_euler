# Consider the following "magic" 3-gon ring, filled with the numbers 1 to 6, and each line adding to nine.

# Working clockwise, and starting from the group of three with the numerically lowest external node(4, 3, 2 in this example), each solution can be described uniquely. For example, the above solution can be described by the set: 4, 3, 2
# 6, 2, 1
# 5, 1, 3.

# It is possible to complete the ring with four different totals: 9, 10, 11, and 12. There are eight solutions in total.

# By concatenating each group it is possible to form 9-digit strings; the maximum string for a 3-gon ring is 432621513.

# Using the numbers 1 to 10, and depending on arrangements, it is possible to form 16- and 17-digit strings. What is the maximum 16-digit string for a "magic" 5-gon ring?

demo_5_gon = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# lines (by index) => (0, 9, 1), (2, 1, 3), (4, 3, 5), (6, 5, 7), (8, 7, 9)

max_possible_order = [6, 9, 8, 7,
max_outer_ring_clockwise = [6, 9, 8, 7, 10]

def validate_5_gon(arr):
    i = arr[0] + arr[9] + arr[2]
    return i


def gon_array_to_line(arr):
    converter = [0, 9, 1, 2, 1, 3, 4, 3, 5, 6, 5, 7, 8, 7, 9]
    line = ''
    for index in converter:
        line += str(arr[index])
    return line


if __name__ == "__main__":
    print(gon_array_to_line(demo_5_gon))
