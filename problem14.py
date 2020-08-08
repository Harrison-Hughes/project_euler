# The following iterative sequence is defined for the set of positive integers:

# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:

# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?
import operator


def longest_collatz_chain_starting_under_n(n):
    length_of_chains = {1: 1}
    for i in range(2, n):
        x = i
        chain = []
        while x > 0:
            if x in length_of_chains:
                for t in range(len(chain)):
                    length_of_chains[chain[t]] = len(
                        chain) - t + length_of_chains[x]
                break
            chain.append(x)
            if x % 2 == 0:
                x = int(x/2)
            else:
                x = 3*x + 1
    return max(length_of_chains.items(), key=operator.itemgetter(1))[0]


if __name__ == "__main__":
    print(longest_collatz_chain_starting_under_n(1000000))
