# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

# 3
# 7 4
# 2 4 6
# 8 5 9 3

# That is, 3 + 7 + 4 + 9 = 23.

# Find the maximum total from top to bottom of the triangle below:


def parse_triangle_string_to_array(triangle):
    [triangle_array, triangle_rows] = [[], triangle.split('\n')]
    for row in triangle_rows:
        split_row = row.split(' ')
        num_row = []
        for i in split_row:
            num_row.append(int(i))
        triangle_array.append(num_row)
    return triangle_array


def maximum_path(triangle):
    triangle_array = parse_triangle_string_to_array(triangle)
    max_dist_triangle = [[triangle_array[0][0]]]
    for i in range(1, len(triangle_array)):
        mdt_row = []
        for t in range(len(triangle_array[i])):
            if t == 0:
                mdt_row.append(triangle_array[i]
                               [t] + max_dist_triangle[i-1][0])
            elif t == len(triangle_array[i-1]):
                mdt_row.append(triangle_array[i]
                               [t] + max_dist_triangle[i-1][t-1])
            else:
                mdt_row.append(
                    max(max_dist_triangle[i-1][t-1],
                        max_dist_triangle[i-1][t]) + triangle_array[i]
                    [t])
        max_dist_triangle.append(mdt_row)
    max_of_final_row = max(max_dist_triangle[-1])
    return max_of_final_row


triangle = '''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''

if __name__ == "__main__":
    print(maximum_path(triangle))
