# By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

# By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.

# Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.

# HARD CODED AND TOO SLOW

import time


def n_member_prime_family(n):
    [numbers, num_length] = [[2], 2]
    cont = True
    while cont:
        def range_starter():
            if num_length == 2:
                return 1
            else:
                return 2
        for i in range(numbers[-1]+range_starter(), 10**num_length, 2):
            numbers.append(i)
        counter = 1
        while counter < len(numbers):
            numbers = [x for x in numbers if x <=
                       numbers[counter] or x % numbers[counter] != 0]
            counter += 1
        prime_value_fam = contains_prime_value_family(numbers, num_length, n)
        # print('prime_value_fam', prime_value_fam)
        if len(prime_value_fam) > 0:
            cont = False
        num_length += 1
    sol = 0
    for i in range(len(prime_value_fam[0])):
        sol += prime_value_fam[0][i] * 10 ** (len(prime_value_fam[0])-i - 1)
    return sol


def contains_prime_value_family(full_arr, digits, family_size):
    correct_length_primes = [x for x in full_arr if len(str(x)) == digits]
    split_primes = []
    for i in correct_length_primes:
        [prime, prime_arr] = [i, []]
        while prime > 0:
            prime_arr.insert(0, prime % 10)
            prime = int(prime/10)
        split_primes.append(prime_arr)

    for digit in range(11 - family_size):
        unfiltered_primes = split_primes
        for prime in split_primes:
            # if digit in prime:
            if how_many_item_in_list(prime[0:-1], digit) == 3:
                indices_of_not_digit = get_anti_indices(prime, digit)
                filtered_primes = [
                    x for x in unfiltered_primes if not_star_match(prime, x, indices_of_not_digit) and star_space_is_repeated_digit(x, indices_of_not_digit)]
                # print('filtered_primes', filtered_primes)
                if len(filtered_primes) == family_size:
                    return filtered_primes
    return []


def how_many_item_in_list(list, item):
    count = 0
    for i in range(len(list)):
        if list[i] == item:
            count += 1
    return count


def not_star_match(base_num, compare_num, anti_indices):
    [base, comparison] = [[], []]
    for i in anti_indices:
        base.append(base_num[i])
        comparison.append(compare_num[i])
    if base == comparison:
        return True
    else:
        return False


def star_space_is_repeated_digit(compare_num, anti_indices):
    star_digit = []
    for i in range(len(compare_num)):
        if i not in anti_indices:
            if star_digit == []:
                star_digit = compare_num[i]
            else:
                if not star_digit == compare_num[i]:
                    return False
    return True


def get_anti_indices(list_, val):
    ret = []
    for i in range(len(list_)):
        if not list_[i] == val:
            ret.append(i)
    return ret


if __name__ == "__main__":
    start_time = time.time()
    print(n_member_prime_family(8))
    print("--- took %s seconds ---" % (time.time() - start_time))


# def contains_prime_value_family(full_arr, digits, family_size):
#     correct_length_primes = [x for x in full_arr if len(str(x)) == digits]
#     split_primes = []
#     for i in correct_length_primes:
#         [prime, prime_arr] = [i, []]
#         while prime > 0:
#             prime_arr.insert(0, prime % 10)
#             prime = int(prime/10)
#         split_primes.append(prime_arr)

#     for x in range(1, 10):
#         for i in range(1, digits):
#             potential_primes = [
#                 n for n in split_primes if n.count(x) == i]
#             filtered_primes = filter_potential_primes(
#                 potential_primes, family_size, x)
#             if filtered_primes != []:
#                 return filtered_primes

#     return 0


# def filter_potential_primes(prime_array, family_size, digit):
#     [primes, filtered_primes] = [prime_array, []]
#     while len(primes) > 0:
#         indices = get_indices(primes[0], digit)
#         filtered_primes = [
#             x for x in prime_array if get_indices(x, digit) == indices]
#         if len(filtered_primes) >= family_size:
#             return filtered_primes
#         else:
#             primes = [x for x in primes if not x in filtered_primes]
#     return []
