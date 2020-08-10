# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

# 3
# 7 4
# 2 4 6
# 8 5 9 3

# That is, 3 + 7 + 4 + 9 = 23.

# Find the maximum total from top to bottom in triangle.txt(right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.
# https: // projecteuler.net/problem=67

# f = open("p067_triangle.txt", "r")
# for x in f:
#     print(x)


def parse_triangle_txtfile_to_array(triangle_file_string):
    [triangle_array, triangle_rows] = [[], []]
    f = open("p067_triangle.txt", "r")
    for x in f:
        triangle_rows.append(x[0:-1])
    f.close()
    for row in triangle_rows:
        split_row = row.split(' ')
        num_row = []
        for i in split_row:
            num_row.append(int(i))
        triangle_array.append(num_row)
    print(triangle_array)
    return triangle_array


def maximum_path(triangle_file_string):
    triangle_array = parse_triangle_txtfile_to_array(triangle_file_string)
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
    print(max_dist_triangle)
    max_of_final_row = max(max_dist_triangle[-1])
    return max_of_final_row


if __name__ == "__main__":
    print(maximum_path("p067_triangle.txt"))
