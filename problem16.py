# 215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

# What is the sum of the digits of the number 2^1000?


def sum_digits_of_2_power_n(n):
    num = 2**n
    sum = 0
    while num > 0:
        sum += num % 10
        num = int(num/10)
    return sum


if __name__ == "__main__":
    print(sum_digits_of_2_power_n(1000))
