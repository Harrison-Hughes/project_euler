# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

# How many such routes are there through a 20×20 grid?


def lattice_paths(dimension):
    lattice = [[1] * (dimension+1)]
    for i in range(1, dimension+1):
        row = [1]
        for t in range(1, dimension+1):
            row.append(row[t-1] + lattice[i-1][t])
        lattice.append(row)
    return lattice[dimension][dimension]


if __name__ == "__main__":
    print(lattice_paths(20))
