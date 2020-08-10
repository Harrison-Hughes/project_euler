# n! means n × (n − 1) × ... × 3 × 2 × 1

# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

# Find the sum of the digits in the number 100!


def sum_digits_of_factorial(n):
    n_fact = 1
    for i in range(1, n+1):
        n_fact *= i
    return sum(map(int, str(n_fact)))


if __name__ == "__main__":
    print(sum_digits_of_factorial(100))
