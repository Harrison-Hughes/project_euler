# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

import numpy


def sumPrimesBelowN(n):
    primeArray = [2]
    i = 3
    while i < n:
        if not nHasFactorInArray(i, primeArray):
            primeArray.append(i)

        i += 1

    return sum(primeArray)


def nHasFactorInArray(n, arr):
    for i in arr:
        if n % i == 0:
            return True
        elif i**2 >= n:
            return False

    return False


if __name__ == "__main__":
    print sumPrimesBelowN(2000000)
