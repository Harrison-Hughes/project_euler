# convergents of e

# Find the sum of digits in the numerator of the 100th convergent of the continued fraction for e

# hard coded for e's unique infinite continued fraction


def fraction_addition(num, frac):
    return [num * frac[1] + frac[0], frac[1]]


def invert_fraction(frac):
    return [frac[1], frac[0]]


def nth_conergent_fraction_of_e(n):
    cont_fraction = []
    for i in range(n):
        if (i-1) % 3 == 0:
            cont_fraction.append(2*(i+2)/3)
        else:
            cont_fraction.append(1)
    sum = [1, cont_fraction[-1]]
    for i in range(1, n-1):
        sum = fraction_addition(cont_fraction[-(i+2)], invert_fraction(sum))
    sum = fraction_addition(2, invert_fraction(sum))

    return sum_of_digits(sum[0])


def sum_of_digits(num):
    return sum(map(int, str(num)))


if __name__ == "__main__":
    print(nth_conergent_fraction_of_e(100))
