# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


# note: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

def number_sequence_letter_total_up_to_n(n):
    total = 0
    for i in range(1, n+1):
        print(i, calc_length_of_num(i))
        total += calc_length_of_num(i)
    return total


def calc_length_of_num(x):
    key_num = {1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 7: 5, 8: 5, 9: 4, 10: 3, 11: 6, 12: 6,
               13: 8, 14: 8, 15: 7, 16: 7, 17: 9, 18: 8, 19: 8, 20: 6, 30: 6, 40: 5, 50: 5, 60: 5, 70: 7, 80: 6, 90: 6, 1000: 11}

    if x == 0:
        return 0

    if x in key_num:
        return key_num[x]

    def calc_length_less_than_100(x):
        if x == 0:
            return x
        return key_num[(int(x/10)*10)] + key_num[int(x % 10)]

    if int(x/100) == 0:  # less than 100
        return calc_length_less_than_100(x)
    else:  # >= 100

        if x % 100 == 0:  # exact divisor of 100
            return key_num[int(x/100)] + 7  # x hundred
        else:
            # x hundred and x
            return key_num[int(x/100)] + 10 + calc_length_of_num(x - 100*int(x/100))


if __name__ == "__main__":
    print(number_sequence_letter_total_up_to_n(1000))
