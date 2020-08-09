# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


# note: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

def number_sequence_letter_total_up_to_n(n):
    total = 0
    for i in range(1, n+1):
        total += calc_length_of_num(i)


def calc_length_of_num(x):
    key_num = {1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 7: 5, 8: 5, 9: 4, 10: 3, 11: 7, 12: 6,
               13: 8, 14: 8, 15: 7, 16: 7, 17: 9, 18: 8, 19: 8, 20: 6, 30: 6, 40: 6, 50: 5, 60: 5, 70: 7, 80: 6, 90: 6}
    if x in key_num:
        if not int(x/100) == 0:
            if x == 100:

                int(x/100)
